from .models import Turmas, Alunos, Nivel_Ensino
from django.contrib.auth.decorators import login_required
from autenticacao.models import Pessoa

def get_turmas(request): 
    if not request.user.is_authenticated:
        return {}   
    
    pessoa = Pessoa.objects.get(user=request.user)
    dict_niveis_ensino = []

    if pessoa.tipo_conta in ['pro', 'dir']:
        niveis_ensino = Nivel_Ensino.objects.filter(
            turmas__escola__professor__user=request.user
        ).distinct() | Nivel_Ensino.objects.filter(
            turmas__escola__diretor__user=request.user
        ).distinct()
        niveis_ensino = niveis_ensino.distinct().order_by('nome')  # Order by name

        for nivel in niveis_ensino:
            turmas_1 = Turmas.objects.filter(nivel_ensino=nivel, escola__professor__user=request.user).distinct()
            turmas_2 = Turmas.objects.filter(nivel_ensino=nivel, escola__diretor__user=request.user).distinct()
            turmas = (turmas_1 | turmas_2).distinct().order_by('nome')  # Order by name
            dict_niveis_ensino.append({'nivel': nivel, 'turmas': turmas})

    elif pessoa.tipo_conta in ['adm', 'ass']:
        niveis_ensino = Nivel_Ensino.objects.all().distinct().order_by('nome')  # Order by name
        for nivel in niveis_ensino:
            turmas = Turmas.objects.filter(nivel_ensino=nivel).distinct().order_by('nome')  # Order by name
            dict_niveis_ensino.append({'nivel': nivel, 'turmas': turmas})

    return {
        'niveis_ensino': dict_niveis_ensino,
        'pessoa': pessoa
    }
