from django import forms
from django.forms import ModelForm

import unicodedata

from django.contrib.auth import (
    get_user_model
)
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.utils.translation import gettext_lazy as _

from .models import *
from .functions import validate_cpf

UserModel = get_user_model()

def _unicode_ci_compare(s1, s2):
    """
    Perform case-insensitive comparison of two identifiers, using the
    recommended algorithm from Unicode Technical Report 36, section
    2.11.2(B)(2).
    """
    return unicodedata.normalize('NFKC', s1).casefold() == unicodedata.normalize('NFKC', s2).casefold()


class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        """
        Send a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')

        email_message.send()

    def get_users(self, email):
        """Given an email, return matching user(s) who should receive a reset.

        This allows subclasses to more easily customize the default policies
        that prevent inactive users and users with unusable passwords from
        resetting their password.
        """
        email_field_name = UserModel.get_email_field_name()
        active_users = UserModel._default_manager.filter(**{
            '%s__iexact' % email_field_name: email,
            'is_active': True,
        })
        return (
            u for u in active_users
            if u.has_usable_password() and
            _unicode_ci_compare(email, getattr(u, email_field_name))
        )

    def save(self, domain_override=None,
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None,
             extra_email_context=None):
        """
        Generate a one-use only link for resetting password and send it to the
        user.
        """
        email = self.cleaned_data["email"]
        if not domain_override:
            current_site = get_current_site(request)
            site_name = current_site.name
            domain = current_site.domain
        else:
            site_name = domain = domain_override
        email_field_name = UserModel.get_email_field_name()
        for user in self.get_users(email):
            user_email = getattr(user, email_field_name)
            context = {
                'email': user_email,
                'domain': domain,
                'site_name': site_name,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': 'https' if use_https else 'http',
                **(extra_email_context or {}),
            }
            self.send_mail(
                subject_template_name, email_template_name, context, from_email,
                user_email, html_email_template_name=html_email_template_name,
            )


class Cadastrar_usuario_form(forms.Form):
    username = forms.CharField(max_length=150, required=True, label='Matricula')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Senha')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmação de senha')
    
class Pessoa_form(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.pessoa = Pessoa.objects.get(user=self.user)
            if self.pessoa.tipo_conta == 'adm':
                # Administrador pode ver todas as opções
                pass
            elif self.pessoa.tipo_conta == 'ass':
                # Assistente Administrativo pode ver opções limitadas
                self.fields['tipo_conta'].choices = [
                    choice for choice in self.fields['tipo_conta'].choices if choice[0] in ['ass', 'dir', 'pro']
                ]
            elif self.pessoa.tipo_conta == 'dir':
                # Diretor pode ver opções limitadas
                self.fields['tipo_conta'].choices = [
                    choice for choice in self.fields['tipo_conta'].choices if choice[0] in ['pro']
                ]
            elif self.pessoa.tipo_conta == 'pro':
                # Professor só pode ver sua própria opção
                self.fields['tipo_conta'].choices = [
                    choice for choice in self.fields['tipo_conta'].choices if choice[0] == 'alu'
                ]

    class Meta:
        model = Pessoa
        fields = [ 'nome', 'cpf', 'email', 'tipo_conta']
        widgets = {
            # 'user': forms.HiddenInput(),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'onkeydown': "mascara(this, icpf)"}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'tipo_conta': forms.Select(attrs={'class': 'form-control'}),
        }


    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        cpf = validate_cpf(cpf)            
        return cpf

