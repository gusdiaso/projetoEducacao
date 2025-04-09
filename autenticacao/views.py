from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordContextMixin
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _

from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError

from .models import *
from .forms import *

from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import (PasswordResetForm, SetPasswordForm)
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import (url_has_allowed_host_and_scheme, urlsafe_base64_decode,)
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from settings.settings import hCAPTCHA_PRIVATE_KEY, hCAPTCHA_PUBLIC_KEY
import requests
from django.contrib.auth.decorators import login_required

def login_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('/')
    

    if request.method == 'POST':

        #  Abaixo recebemos a validação da API do Google do reCAPTCHA
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('h-captcha-response')
        data = {
            'secret': hCAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://hcaptcha.com/siteverify', data=data)
        result = r.json()
        ''' End reCAPTCHA validation '''
        # result={'success': True}
        
        # if not result['success']:
        if False:
            messages.error(request, 'Por favor, confirme que você não é um robô.')
            context = {
                'hCAPTCHA': hCAPTCHA_PUBLIC_KEY,
            }
            return render(request, 'adm/new_login.html', context)
        
        username = request.POST['username']
        password = request.POST['password']
        # if len(username)==5 and username.isdigit():
        #     username = '0'+username
        try:
            user = authenticate(request, username=username, password=password)
        except:            
            user = None

        if user is not None:
            login(request, user)
            next_url = request.POST.get('next')
            
            # Verifica se a URL é segura
            if url_has_allowed_host_and_scheme(next_url, allowed_hosts=request.get_host()):
                return redirect(next_url)
            else:
                print("URL não segura, redirecionando para a página inicial.")
                return redirect('autenticacao:painel_administrativo')
        else:
            if User.objects.filter(username=username).exists():
                msg = 'Login ou senha invalidos'
            else:
                msg = 'Usuário não cadastrado. Por favor, cadastre-se.'
            
            context = {
                'error': True,
                'msg': msg,
                'hCAPTCHA': hCAPTCHA_PUBLIC_KEY,
            }
    else:
        context = {
            'hCAPTCHA': hCAPTCHA_PUBLIC_KEY,
        }   
        
    return render(request, 'adm/new_login.html', context)

def passwd_reset(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(email=data)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Solicitação de alteração de senha do sistema INTRANET"
                    email_template_name = "adm/email_passwd_reset.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'https',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, user.email, [
                                  user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("autenticacao:passwd_reset_done")
            else:
                messages.error(request, 'Email não cadastrado no sistema.')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="adm/passwd_reset.html", context={"password_reset_form": password_reset_form})

class PasswordResetDoneView(PasswordContextMixin, TemplateView):
    template_name = 'adm/passwd_reset_done.html'
    title = _('Password reset sent')
    
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login')
    else:
        return redirect('/')

INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'

class PasswordResetConfirmView(PasswordContextMixin, FormView):
    form_class = SetPasswordForm
    post_reset_login = False
    post_reset_login_backend = None
    reset_url_token = 'set-password'
    success_url = reverse_lazy('autenticacao:passwd_reset_complete')
    template_name = 'adm/passwd_reset_confirm.html'
    title = _('Entre com a nova senha')
    token_generator = default_token_generator

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        assert 'uidb64' in kwargs and 'token' in kwargs

        self.validlink = False
        self.user = self.get_user(kwargs['uidb64'])

        if self.user is not None:
            token = kwargs['token']
            if token == self.reset_url_token:
                session_token = self.request.session.get(INTERNAL_RESET_SESSION_TOKEN)
                if self.token_generator.check_token(self.user, session_token):
                   
                    self.validlink = True
                    return super().dispatch(*args, **kwargs)
            else:
                if self.token_generator.check_token(self.user, token):
                    self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
                    redirect_url = self.request.path.replace(token, self.reset_url_token)
                    return HttpResponseRedirect(redirect_url)
        
        return self.render_to_response(self.get_context_data())

    def get_user(self, uidb64):
        try:            
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist, ValidationError):
            user = None
        return user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.user
        return kwargs

    def form_valid(self, form):
        user = form.save()
        del self.request.session[INTERNAL_RESET_SESSION_TOKEN]
        if self.post_reset_login:
            auth_login(self.request, user, self.post_reset_login_backend)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.validlink:
            context['validlink'] = True
        else:
            context.update({
                'form': None,
                'title': _('Falha ao redefinir a senha.'),
                'validlink': False,
            })
        return context

class PasswordResetCompleteView(PasswordContextMixin, TemplateView):
    template_name = 'adm/passwd_reset_complete.html'
    title = _('Senha redefinida')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_url'] = resolve_url(settings.LOGIN_URL)
        return context
    

#####################################################################
'''
Comentario sagaz
'''
#####################################################################

# @login_required
# def meio_autenticacao(request, next=None):
#     user = request.user

#     admin = Administrador.objects.filter(user=user)
#     if admin.exists():
#         return redirect('adm') 

@login_required
def painel_administrativo(request):
    return render(request, 'adm/painel_administrativo.html')

@login_required
def administrador_listar(request):
    context = {
        'administradores': Administrador.objects.all()
    }
    return render(request, 'adm/administrador_listar.html', context)

@login_required
def administrador_adicionar(request):
    if request.method == 'POST':
        form = administrador_form(request.POST)
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if not password1 == password2: 
            usuario_form = cadastrar_usuario_form(request.POST)
            usuario_form.add_error('password1', 'As senhas não conferem.')
        
        elif len(password1) <= 8:
            usuario_form = cadastrar_usuario_form(request.POST)
            usuario_form.add_error('password1', 'A senha deve conter pelo menos 8 caracteres.')
        
        elif form.is_valid():
           user = User.objects.create_user(username=username, password=password1)
           user.save()
           adm = form.save()
           adm.user = user
           adm.save()

           return redirect('autenticacao:administrador')
        else:
            usuario_form = cadastrar_usuario_form(request.POST)
    else:
        usuario_form = cadastrar_usuario_form()
        form = administrador_form()
        
    context = {
        'form': form ,
        'form_usuario': usuario_form,
    }
    return render(request, 'adm/administrador_adicionar.html', context)

@login_required
def administrador_editar(request, id):
    if request.method == 'POST':
        form = administrador_form(request.POST)
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(request.POST)
        
        if not password1 == password2: 
            usuario_form = cadastrar_usuario_form(request.POST)
            usuario_form.add_error('password1', 'As senhas não conferem.')
        
        elif len(password1) <= 8:
            usuario_form = cadastrar_usuario_form(request.POST)
            usuario_form.add_error('password1', 'A senha deve conter pelo menos 8 caracteres.')
        
        elif form.is_valid():
            instancia = Administrador.objects.get(id=id)
            form_editado = administrador_form(request.POST, instance=instancia)
            form_editado.save()
            return redirect('autenticacao:administrador')
        else:
            usuario_form = cadastrar_usuario_form(request.POST)
    else:
        usuario_form = cadastrar_usuario_form()
        form = administrador_form()
        
    context = {
        'form': form ,
        'form_usuario': usuario_form,
    }
    return render(request, 'adm/administrador_editar.html', context)


@login_required
def diretor_listar(request):
    context = {
        'diretores': Diretor.objects.all(),
    }
    return render(request, 'adm/diretor_listar.html', context)

@login_required
def professor_listar(request):
    context = {
        'professores': Professor.objects.all(),
    }
    return render(request, 'adm/professor_listar.html', context)

@login_required
def assistente_administrativo_listar(request):
    context = {
        'assistentes_administrativos': Assistente_Administrativo.objects.all(),
    }
    return render(request, 'adm/assistente_administrativo_listar.html', context)

@login_required
def assistente_administrativo_adicionar(request):
    if request.method == 'POST':
        form = Administrador_form(request.POST)
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if not password1 == password2: 
            usuario_form = cadastrar_usuario_form(request.POST)
            usuario_form.add_error('password1', 'As senhas não conferem.')
        
        elif len(password1) <= 8:
            usuario_form = cadastrar_usuario_form(request.POST)
            usuario_form.add_error('password1', 'A senha deve conter pelo menos 8 caracteres.')
        
        elif form.is_valid():
           user = User.objects.create_user(username=username, password=password1)
           user.save()
           adm = form.save()
           adm.user = user
           adm.save()

           return redirect('autenticacao:Administrador')
        else:
            usuario_form = cadastrar_usuario_form(request.POST)
    else:
        usuario_form = cadastrar_usuario_form()
        form = Administrador_form()
        
    context = {
        'form': form ,
        'form_usuario': usuario_form,
    }
    return render(request, 'adm/Administrador_adicionar.html', context)

@login_required
def Administrador_editar(request, id):
    if request.method == 'POST':
        form = Administrador_form(request.POST)
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(request.POST)
        
        if not password1 == password2: 
            usuario_form = cadastrar_usuario_form(request.POST)
            usuario_form.add_error('password1', 'As senhas não conferem.')
        
        elif len(password1) <= 8:
            usuario_form = cadastrar_usuario_form(request.POST)
            usuario_form.add_error('password1', 'A senha deve conter pelo menos 8 caracteres.')
        
        elif form.is_valid():
            instancia = Administrador.objects.get(id=id)
            form_editado = Administrador_form(request.POST, instance=instancia)
            form_editado.save()
            return redirect('autenticacao:Administrador')
        else:
            usuario_form = cadastrar_usuario_form(request.POST)
    else:
        usuario_form = cadastrar_usuario_form()
        form = Administrador_form()
        
    context = {
        'form': form ,
        'form_usuario': usuario_form,
    }
    return render(request, 'adm/Administrador_editar.html', context)



@login_required
def assistente_administrativo_cadastro(request):
    context = {
    }
    return render(request, 'adm/assistente_administrativo_listar.html', context)