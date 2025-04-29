from .models import Turmas, Alunos, Nivel_Ensino
from django.contrib.auth.decorators import login_required
from autenticacao.models import Pessoa

def get_turmas(request): 
    if not request.user.is_authenticated:
        return {}   
    
    pessoa = Pessoa.objects.get(user=request.user)
    dict_niveis_ensino = []

    if pessoa.tipo_conta == 'pro':
        # Professor: Access to all levels and classes in their school
        niveis_ensino = Nivel_Ensino.objects.filter(turmas__escola__turmas__professor=pessoa).distinct()
        for nivel in niveis_ensino:
            turmas = Turmas.objects.filter(escola__turmas__professor=pessoa, nivel_ensino=nivel).distinct()
            dict_niveis_ensino.append({'nivel': nivel, 'turmas': turmas})

    elif pessoa.tipo_conta == 'dir':
        # Director: Access to all levels and classes in their school
        niveis_ensino = Nivel_Ensino.objects.filter(turmas__escola__diretor=pessoa).distinct()
        for nivel in niveis_ensino:
            turmas = Turmas.objects.filter(escola__diretor=pessoa, nivel_ensino=nivel).distinct()
            dict_niveis_ensino.append({'nivel': nivel, 'turmas': turmas})

    elif pessoa.tipo_conta in ['ass', 'adm']:
        # Administrative Assistant and Administrator: Access to all levels and classes in all schools
        niveis_ensino = Nivel_Ensino.objects.all().distinct()
        for nivel in niveis_ensino:
            turmas = Turmas.objects.filter(nivel_ensino=nivel).distinct()
            dict_niveis_ensino.append({'nivel': nivel, 'turmas': turmas})

    return {'niveis_ensino': dict_niveis_ensino, 'pessoa': pessoa}

