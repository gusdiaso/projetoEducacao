from functools import wraps
from django.http import HttpResponseForbidden
from .models import Pessoa

def required_nivel_administrador(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        pessoa = Pessoa.objects.filter(user=request.user)
        if pessoa.exists() and (pessoa.first().tipo_conta == 'adm'):
            
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Acesso restrito ao administrador.")
    return _wrapped_view

def required_nivel_assistente_administrativo(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        pessoa = Pessoa.objects.filter(user=request.user)
        if pessoa.exists() and (pessoa.first().tipo_conta == 'adm' or pessoa.first().tipo_conta == 'ass'):
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Acesso restrito ao assistente administrativo ou superior.")
    return _wrapped_view

def required_nivel_diretor(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        pessoa = Pessoa.objects.filter(user=request.user)
        if pessoa.exists() and (pessoa.first().tipo_conta == 'adm' or pessoa.first().tipo_conta == 'ass' or pessoa.first().tipo_conta == 'dir'):
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Acesso restrito ao diretor ou superior.")
    return _wrapped_view

def required_nivel_professor(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        pessoa = Pessoa.objects.filter(user=request.user)
        if pessoa.exists() and (pessoa.first().tipo_conta == 'adm' or pessoa.first().tipo_conta == 'ass' or pessoa.first().tipo_conta == 'dir' or pessoa.first().tipo_conta == 'pro'):
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Acesso restrito ao professor.")
    return _wrapped_view
