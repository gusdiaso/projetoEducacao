from .models import Turmas, Alunos, Nivel_Ensino
from django.contrib.auth.decorators import login_required
from autenticacao.models import Pessoa
def get_turmas(request): 
    if not request.user.is_authenticated:
        return {}   
    
    niveis_ensino = Nivel_Ensino.objects.filter(turmas__professor__user=request.user).distinct()
    dict_niveis_ensino =[]
    for nivel in niveis_ensino:
        turmas = Turmas.objects.filter(nivel_ensino=nivel, professor__user=request.user).distinct()
        dict_niveis_ensino.append({'nivel': nivel, 'turmas': turmas})
    return {'niveis_ensino': dict_niveis_ensino, 'pessoa': Pessoa.objects.get(user=request.user)}

