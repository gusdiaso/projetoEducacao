from .models import Turmas, Alunos, Nivel_Ensino
from django.contrib.auth.decorators import login_required
from autenticacao.models import Pessoa

# Se for professor, ele terá acesso a todas as turmas e niveis de ensino da escola que ele é professor
# Se for diretor, ele terá acesso a todas as turmas e niveis de ensino da escola que ele é diretor
# Se for assistente administrativo, ele terá acesso a todas as turmas e niveis de ensino de todas as escolas
# Se for administrador, ele terá acesso a todas as turmas e niveis de ensino de todas as escolas

def get_turmas(request): 
    if not request.user.is_authenticated:
        return {}   
    
    niveis_ensino = Nivel_Ensino.objects.filter(turmas__professor__user=request.user).distinct()
    dict_niveis_ensino =[]
    for nivel in niveis_ensino:
        turmas_1 = Turmas.objects.filter(nivel_ensino=nivel, professor__user=request.user).distinct()
        turmas_2 = Turmas.objects.filter(nivel_ensino=nivel, escola__diretor__user=request.user).distinct()
        turmas = turmas_1 | turmas_2
        turmas = turmas.distinct()
        dict_niveis_ensino.append({'nivel': nivel, 'turmas': turmas})
    return {'niveis_ensino': dict_niveis_ensino, 'pessoa': Pessoa.objects.get(user=request.user)}

