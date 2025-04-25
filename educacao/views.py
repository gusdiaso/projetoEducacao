from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tipo_Avaliacoes, Escolas, Nivel_Ensino, Avaliacoes, Turmas, Alunos
from .forms import TipoAvaliacoesForm, EscolasEditForm, EscolasForm, NivelEnsinoForm, AvaliacoesForm, TurmasForm, AlunosForm
from django.http import FileResponse, Http404
from autenticacao.models import Pessoa
from django.http import FileResponse
import os

@login_required
def index(request):
    return render(request, 'educacao/index.html')

#TIPO AVALIAÇÕES
@login_required
def tipo_avaliacoes_list(request):
    tipos = Tipo_Avaliacoes.objects.all()
    return render(request, 'tipo_ensino/tipo_avaliacoes_list.html', {'tipos': tipos})

@login_required
def tipo_avaliacoes_create(request):
    if request.method == 'POST':
        form = TipoAvaliacoesForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('educacao:tipo_avaliacoes_list')
    else:
        form = TipoAvaliacoesForm(user=request.user)
    return render(request, 'tipo_ensino/tipo_avaliacoes_form.html', {'form': form})

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
    return render(request, 'tipo_ensino/tipo_avaliacoes_form.html', {'form': form})

@login_required
def tipo_avaliacoes_delete(request, pk):
    tipo = get_object_or_404(Tipo_Avaliacoes, pk=pk)
    if request.method == 'POST':
        tipo.delete()
        return redirect('educacao:tipo_avaliacoes_list')
    return render(request, 'tipo_ensino/tipo_avaliacoes_confirm_delete.html', {'tipo': tipo})

#ESCOLAS
@login_required
def escolas_list(request):
    escolas = Escolas.objects.all()
    return render(request, 'educacao/escolas/escolas_list.html', {'escolas': escolas})

@login_required
def escolas_list_educacao(request):
    escolas = Escolas.objects.all()
    return render(request, 'educacao/escolas/escolas_list_educacao.html', {'escolas': escolas})


@login_required
def escolas_create(request):
    if request.method == 'POST':
        form = EscolasForm(request.POST, user=request.user)
        if form.is_valid():
            escola = form.save()
            escola.user_inclusao = request.user
            escola.save()
            return redirect('educacao:escolas_list')
    else:
        form = EscolasForm(user=request.user)
    return render(request, 'educacao/escolas/escolas_form.html', {'form': form})

@login_required
def escolas_update(request, pk):
    escola = get_object_or_404(Escolas, pk=pk)
    if request.method == 'POST':
        form = EscolasEditForm(request.POST, instance=escola, user=request.user)
        if form.is_valid():
            escola = form.save()
            return redirect('educacao:escolas_list')
    else:
        form = EscolasForm(instance=escola, user=request.user)
    return render(request, 'educacao/escolas/escolas_form.html', {'form': form})

@login_required
def escolas_delete(request, pk):
    escola = get_object_or_404(Escolas, pk=pk)
    if request.method == 'POST':
        escola.delete()
        return redirect('educacao:escolas_list')
    return render(request, 'educacao/escolas/escolas_confirm_delete.html', {'escola': escola})

#NIVEL ENSINO
@login_required
def nivel_ensino_list(request):
    niveis = Nivel_Ensino.objects.all()
    return render(request, 'nivel_ensino/nivel_ensino_list.html', {'niveis': niveis})

@login_required
def nivel_ensino_create(request):
    if request.method == 'POST':
        form = NivelEnsinoForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('educacao:nivel_ensino_list')
    else:
        form = NivelEnsinoForm(user=request.user)
    return render(request, 'nivel_ensino/nivel_ensino_form.html', {'form': form})

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
    return render(request, 'nivel_ensino/nivel_ensino_form.html', {'form': form})

@login_required
def nivel_ensino_delete(request, pk):
    nivel = get_object_or_404(Nivel_Ensino, pk=pk)
    if request.method == 'POST':
        nivel.delete()
        return redirect('educacao:nivel_ensino_list')
    return render(request, 'nivel_ensino/nivel_ensino_confirm_delete.html', {'nivel': nivel})

#AVALIAÇÕES
@login_required
def avaliacoes_list(request):
    avaliacoes = Avaliacoes.objects.all()
    return render(request, 'educacao/avaliacoes/avaliacoes_list.html', {'avaliacoes': avaliacoes})

@login_required
def avaliacao_download(request, id):
    avaliacao = get_object_or_404(Avaliacoes, id=id)
    tipo_de_avaliacao = avaliacao.tipo_avaliacao 
    file_path = tipo_de_avaliacao.arquivo.path  

    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
        return response
    else:
        raise Http404("File does not exist")

@login_required
def avaliacoes_create(request):
    if request.method == 'POST':
        form = AvaliacoesForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('educacao:tipo_avaliacoes_list')
    else:
        form = AvaliacoesForm(user=request.user)
    return render(request, 'educacao/avaliacoes/avaliacoes_form.html', {'form': form})

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
    return render(request, 'educacao/avaliacoes/avaliacoes_form.html', {'form': form})

@login_required
def avaliacoes_delete(request, pk):
    avaliacao = get_object_or_404(Avaliacoes, pk=pk)
    if request.method == 'POST':
        avaliacao.delete()
        return redirect('educacao:avaliacoes_list')
    return render(request, 'educacao/avaliacoes/avaliacoes_confirm_delete.html', {'avaliacao': avaliacao})


#TURMAS
@login_required
def turmas_list(request):
    turmas = Turmas.objects.all()
    return render(request, 'educacao/turmas/turmas_list.html', {'turmas': turmas})

@login_required
def escola_list_turmas(request, escola_id):
    escola = get_object_or_404(Escolas, pk=escola_id)
    turmas = Turmas.objects.filter(escola=escola)
    return render(request, 'educacao/turmas/turmas_list.html', {'turmas': turmas, 'escola': escola})


login_required
def turma(request, turma_id):
    turma = get_object_or_404(Turmas, pk=turma_id)
    alunos = Alunos.objects.filter(turma=turma)
    return render(request, 'educacao/turmas/turma.html', {'turma': turma, 'alunos': alunos})

@login_required
def turmas_create(request):
    if request.method == 'POST':
        form = TurmasForm(request.POST, user=request.user)
        if form.is_valid():
            turma = form.save()         
            # pessoa = Pessoa.objects.get(user=request.user)
            # turma.professor = pessoa if pessoa.is_professor() else None
            # turma.save()
            return redirect('educacao:turma', turma_id=turma.id)
    else:
        form = TurmasForm(user=request.user)
    return render(request, 'educacao/turmas/turmas_form.html', {'form': form})

@login_required
def turmas_update(request, pk):
    turma = get_object_or_404(Turmas, pk=pk)
    if request.method == 'POST':
        form = TurmasForm(request.POST, instance=turma)
        if form.is_valid():
            turma = form.save()         
            # pessoa = Pessoa.objects.get(user=request.user)
            # turma.professor = pessoa if pessoa.is_professor() else None
            # turma.save()
            return redirect('educacao:turma', turma_id=turma.id)
    else:
        form = TurmasForm(instance=turma, user=request.user)
    return render(request, 'educacao/turmas/turmas_form.html', {'form': form, 'turma': turma})


@login_required
def turmas_delete(request, pk):
    turma = get_object_or_404(Turmas, pk=pk)
    if request.method == 'POST':
        turma.delete()
        return redirect('educacao:turmas_list')
    return render(request, 'educacao/turmas/turmas_confirm_delete.html', {'turma': turma})

#Gerenciamento da Turma
@login_required
def alunos_create(request, turma_id):
    turma = get_object_or_404(Turmas, pk=turma_id)
    if request.method == 'POST':
        form = AlunosForm(request.POST, user=request.user)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.turma = turma
            aluno.save()
            return redirect('educacao:turma', turma_id=turma.id)
    else:
        form = AlunosForm(user=request.user)
    return render(request, 'educacao/alunos/alunos_form.html', {'form': form, 'turma': turma})

@login_required
def alunos_delete(request, pk, turma_id):
    aluno = get_object_or_404(Alunos, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('educacao:turma', turma_id=turma_id)
    return render(request, 'educacao/alunos/alunos_confirm_delete.html', {'aluno': aluno, 'turma_id': turma_id})

#VIEWS QUE NÃO DEVERIAM EXISTIR

@login_required
def turmas_list_escola(request, id):
    escola = Escolas.objects.get(id=id)
    turmas_selected = Turmas.objects.filter(escola__id=escola)
    return render(request, 'educacao/turmas/turmas_list_educacao.html', {'turmas': turmas_selected})

@login_required
def avaliacoes_list_educacao(request, ensino_id):
    nivel_ensino = Nivel_Ensino.objects.get(id=ensino_id)
    avaliacoes_selected = Avaliacoes.objects.filter(nivel_ensino=nivel_ensino)
    return render(request, 'educacao/avaliacoes/avaliacao_list_educacao.html', {'avaliacoes': avaliacoes_selected})

# @login_required
# def avaliacoes_list_educacao(request, ensino_id, avaliacao_id):
#     documento = Tipo_Avaliacoes.objects.get(id=avaliacao_id)
#     nivel_ensino = Nivel_Ensino.objects.get(id=ensino_id)
#     avaliacoes_selected = Avaliacoes.objects.filter(nivel_ensino=nivel_ensino)
#     return render(request, 'educacao/avaliacoes/avaliacao_list_educacao.html', {'avaliacoes': avaliacoes_selected, 'documento': documento})
