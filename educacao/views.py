from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tipo_Avaliacoes, Escolas, Nivel_Ensino, Avaliacoes, Turmas, Alunos
from .forms import TipoAvaliacoesForm, EscolasForm, NivelEnsinoForm, AvaliacoesForm, TurmasForm, AlunosForm

# Create your views here.
@login_required
def index(request):
    
    return render(request, 'educacao/index.html')

@login_required
def tipo_avaliacoes_list(request):
    tipos = Tipo_Avaliacoes.objects.all()
    return render(request, 'educacao/tipo_avaliacoes_list.html', {'tipos': tipos})

@login_required
def tipo_avaliacoes_create(request):
    if request.method == 'POST':
        form = TipoAvaliacoesForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('educacao:tipo_avaliacoes_list')
    else:
        form = TipoAvaliacoesForm(user=request.user)
    return render(request, 'educacao/tipo_avaliacoes_form.html', {'form': form})

@login_required
def tipo_avaliacoes_update(request, pk):
    tipo = get_object_or_404(Tipo_Avaliacoes, pk=pk)
    if request.method == 'POST':
        form = TipoAvaliacoesForm(request.POST, request.FILES, instance=tipo, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('educacao:tipo_avaliacoes_list')
    else:
        form = TipoAvaliacoesForm(instance=tipo, user=request.user)
    return render(request, 'educacao/tipo_avaliacoes_form.html', {'form': form})

@login_required
def tipo_avaliacoes_delete(request, pk):
    tipo = get_object_or_404(Tipo_Avaliacoes, pk=pk)
    if request.method == 'POST':
        tipo.delete()
        return redirect('educacao:tipo_avaliacoes_list')
    return render(request, 'educacao/tipo_avaliacoes_confirm_delete.html', {'tipo': tipo})

@login_required
def escolas_list(request):
    escolas = Escolas.objects.all()
    return render(request, 'educacao/escolas_list.html', {'escolas': escolas})

@login_required
def escolas_list_educacao(request):
    escolas = Escolas.objects.all()
    return render(request, 'educacao/escolas_list_educacao.html', {'escolas': escolas})


@login_required
def escolas_create(request):
    if request.method == 'POST':
        form = EscolasForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('educacao:escolas_list')
    else:
        form = EscolasForm(user=request.user)
    return render(request, 'educacao/escolas_form.html', {'form': form})

@login_required
def escolas_update(request, pk):
    escola = get_object_or_404(Escolas, pk=pk)
    if request.method == 'POST':
        form = EscolasForm(request.POST, instance=escola, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('educacao:escolas_list')
    else:
        form = EscolasForm(instance=escola, user=request.user)
    return render(request, 'educacao/escolas_form.html', {'form': form})

@login_required
def escolas_delete(request, pk):
    escola = get_object_or_404(Escolas, pk=pk)
    if request.method == 'POST':
        escola.delete()
        return redirect('educacao:escolas_list')
    return render(request, 'educacao/escolas_confirm_delete.html', {'escola': escola})

@login_required
def nivel_ensino_list(request):
    niveis = Nivel_Ensino.objects.all()
    return render(request, 'educacao/nivel_ensino_list.html', {'niveis': niveis})

@login_required
def nivel_ensino_create(request):
    if request.method == 'POST':
        form = NivelEnsinoForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('educacao:nivel_ensino_list')
    else:
        form = NivelEnsinoForm(user=request.user)
    return render(request, 'educacao/nivel_ensino_form.html', {'form': form})

@login_required
def nivel_ensino_update(request, pk):
    nivel = get_object_or_404(Nivel_Ensino, pk=pk)
    if request.method == 'POST':
        form = NivelEnsinoForm(request.POST, instance=nivel, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('educacao:nivel_ensino_list')
    else:
        form = NivelEnsinoForm(instance=nivel, user=request.user)
    return render(request, 'educacao/nivel_ensino_form.html', {'form': form})

@login_required
def nivel_ensino_delete(request, pk):
    nivel = get_object_or_404(Nivel_Ensino, pk=pk)
    if request.method == 'POST':
        nivel.delete()
        return redirect('educacao:nivel_ensino_list')
    return render(request, 'educacao/nivel_ensino_confirm_delete.html', {'nivel': nivel})

@login_required
def avaliacoes_list(request):
    avaliacoes = Avaliacoes.objects.all()
    return render(request, 'educacao/avaliacoes_list.html', {'avaliacoes': avaliacoes})

@login_required
def avaliacoes_create(request):
    if request.method == 'POST':
        form = AvaliacoesForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('educacao:avaliacoes_list')
    else:
        form = AvaliacoesForm(user=request.user)
    return render(request, 'educacao/avaliacoes_form.html', {'form': form})

@login_required
def avaliacoes_update(request, pk):
    avaliacao = get_object_or_404(Avaliacoes, pk=pk)
    if request.method == 'POST':
        form = AvaliacoesForm(request.POST, instance=avaliacao, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('educacao:avaliacoes_list')
    else:
        form = AvaliacoesForm(instance=avaliacao, user=request.user)
    return render(request, 'educacao/avaliacoes_form.html', {'form': form})

@login_required
def avaliacoes_delete(request, pk):
    avaliacao = get_object_or_404(Avaliacoes, pk=pk)
    if request.method == 'POST':
        avaliacao.delete()
        return redirect('educacao:avaliacoes_list')
    return render(request, 'educacao/avaliacoes_confirm_delete.html', {'avaliacao': avaliacao})

@login_required
def avaliacoes_list_educacao(request, ensino_id):
    nivel_ensino = Nivel_Ensino.objects.get(id=ensino_id)
    avaliacoes_selected = Avaliacoes.objects.filter(nivel_ensino=nivel_ensino)
    return render(request, 'educacao/avaliacao_list_educacao.html', {'avaliacoes': avaliacoes_selected})

@login_required
def avaliacoes_list_educacao(request, ensino_id):
    nivel_ensino = Nivel_Ensino.objects.get(id=ensino_id)
    avaliacoes_selected = Avaliacoes.objects.filter(nivel_ensino=nivel_ensino)
    return render(request, 'educacao/avaliacao_list_educacao.html', {'avaliacoes': avaliacoes_selected})


@login_required
def turmas_list(request):
    turmas = Turmas.objects.all()
    return render(request, 'educacao/turmas_list.html', {'turmas': turmas})



@login_required
def turmas_create(request):
    if request.method == 'POST':
        form = TurmasForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('educacao:turmas_list')
    else:
        form = TurmasForm(user=request.user)
    return render(request, 'educacao/turmas_form.html', {'form': form})

@login_required
def turmas_update(request, pk):
    turma = get_object_or_404(Turmas, pk=pk)
    if request.method == 'POST':
        form = TurmasForm(request.POST, instance=turma, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('educacao:turmas_list')
    else:
        form = TurmasForm(instance=turma, user=request.user)
    return render(request, 'educacao/turmas_form.html', {'form': form})


@login_required
def turmas_list_educacao(request, ensino_id):
    nivel_ensino = Nivel_Ensino.objects.get(id=ensino_id)
    turmas_selected = Turmas.objects.filter(nivel_ensino=nivel_ensino, professor__user=request.user)
    return render(request, 'educacao/turmas_list_educacao.html', {'turmas': turmas_selected})


@login_required
def turmas_list_escola(request, id):
    escola = Escolas.objects.get(id=id)
    turmas_selected = Turmas.objects.filter(escola__id=escola)
    return render(request, 'educacao/turmas_list_educacao.html', {'turmas': turmas_selected})



@login_required
def turmas_delete(request, pk):
    turma = get_object_or_404(Turmas, pk=pk)
    if request.method == 'POST':
        turma.delete()
        return redirect('educacao:turmas_list')
    return render(request, 'educacao/turmas_confirm_delete.html', {'turma': turma})

@login_required
def alunos_list(request, turma_id):
    turma = get_object_or_404(Turmas, pk=turma_id)
    alunos = Alunos.objects.filter(turma=turma)
    return render(request, 'educacao/alunos_list.html', {'turma': turma, 'alunos': alunos})

@login_required
def alunos_create(request, turma_id):
    turma = get_object_or_404(Turmas, pk=turma_id)
    if request.method == 'POST':
        form = AlunosForm(request.POST, user=request.user)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.turma = turma
            aluno.save()
            return redirect('educacao:alunos_list', turma_id=turma.id)
    else:
        form = AlunosForm(user=request.user)
    return render(request, 'educacao/alunos_form.html', {'form': form, 'turma': turma})

@login_required
def alunos_delete(request, pk, turma_id):
    aluno = get_object_or_404(Alunos, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('educacao:alunos_list', turma_id=turma_id)
    return render(request, 'educacao/alunos_confirm_delete.html', {'aluno': aluno, 'turma_id': turma_id})
