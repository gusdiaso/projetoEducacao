from .models import Turmas, Alunos, Nivel_Ensino
from django.contrib.auth.decorators import login_required

@login_required
def get_turmas(request):    
    turmas = Turmas.objects.filter(professor__user=request.user)
    niveis_ensino = Nivel_Ensino.objects.filter(turmas__professor__user=request.user).distinct()
    return {'turmas': turmas, 'niveis_ensino': niveis_ensino}

