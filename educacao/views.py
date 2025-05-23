from django.shortcuts import render, redirect, get_object_or_404
import unicodedata
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Tipo_Avaliacoes, Escolas, Nivel_Ensino, Avaliacoes, Turmas, Alunos, Componente_Curricular, Aluno_Turma, Resultado_Avaliacoes, Observacoes_Aluno

from .forms import TipoAvaliacoesForm, EscolasEditForm, EscolasForm, NivelEnsinoForm, AvaliacoesForm, TurmasForm, AlunosForm, ObservacoesAlunoForm, ResultadoAvaliacoesForm, ComponenteCurricularForm, AlunosTurmasForm

from autenticacao.decorators import required_nivel_administrador, required_nivel_assistente_administrativo, required_nivel_diretor, required_nivel_professor

@login_required
def index(request):
    return render(request, 'educacao/index.html')

#TIPO AVALIAÇÕES
@login_required
@required_nivel_professor
def tipo_avaliacoes_list(request):
    tipos = Tipo_Avaliacoes.objects.all()
    
    return render(request, 'tipo_ensino/tipo_avaliacoes_list.html', {'tipos': tipos})

@login_required
@required_nivel_professor
def tipo_avaliacoes_create(request):
    if request.method == 'POST':
        form = TipoAvaliacoesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('educacao:tipo_avaliacoes_list')
        else:
            print(form.errors)
    else:
        form = TipoAvaliacoesForm(initial={'user_inclusao': request.user, 'user_edicao': request.user})
    return render(request, 'tipo_ensino/tipo_avaliacoes_form.html', {'form': form})

@login_required
@required_nivel_diretor
def tipo_avaliacoes_update(request, pk):
    tipo = get_object_or_404(Tipo_Avaliacoes, pk=pk)
    print(tipo)
    if request.method == 'POST':
        form = TipoAvaliacoesForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('educacao:tipo_avaliacoes_list')
    else:
        form = TipoAvaliacoesForm(instance=tipo, initial={'user_edicao': tipo.user_edicao})
    return render(request, 'tipo_ensino/tipo_avaliacoes_form.html', {'form': form})

@login_required
@required_nivel_diretor
def tipo_avaliacoes_delete(request, pk):
    tipo = get_object_or_404(Tipo_Avaliacoes, pk=pk)
    if request.method == 'POST':
        tipo.delete()
        return redirect('educacao:tipo_avaliacoes_list')
    return render(request, 'tipo_ensino/tipo_avaliacoes_confirm_delete.html', {'tipo': tipo})

#ESCOLAS
@login_required
@required_nivel_assistente_administrativo
def escolas_list(request):
    escolas = Escolas.objects.all()
    return render(request, 'educacao/escolas/escolas_list.html', {'escolas': escolas})

@login_required
@required_nivel_assistente_administrativo
def escolas_list_educacao(request):
    escolas = Escolas.objects.all()
    return render(request, 'educacao/escolas/escolas_list_educacao.html', {'escolas': escolas})


@login_required
@required_nivel_assistente_administrativo
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
@required_nivel_administrador
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
@required_nivel_administrador
def escolas_delete(request, pk):
    escola = get_object_or_404(Escolas, pk=pk)
    if request.method == 'POST':
        escola.delete()
        return redirect('educacao:escolas_list')
    return render(request, 'educacao/escolas/escolas_confirm_delete.html', {'escola': escola})


#COMPONENTE CURRICULAR
@login_required
@required_nivel_assistente_administrativo
def componente_curricular_list(request):
    componente_curricular = Componente_Curricular.objects.all()
    return render(request, 'componente_curricular/componente_curricular.html', {'componente_curricular': componente_curricular})

@login_required
@required_nivel_assistente_administrativo
def componente_curricular_create(request):
    if request.method == 'POST':
        form = ComponenteCurricularForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('educacao:componente_curricular_list')
    else:
        form = ComponenteCurricularForm(user=request.user)
    return render(request, 'componente_curricular/componente_curricular_form.html', {'form': form})

@login_required
@required_nivel_administrador
def componente_curricular_update(request, pk):
    componente_curricular = get_object_or_404(Componente_Curricular, pk=pk)
    if request.method == 'POST':
        form = ComponenteCurricularForm(request.POST, instance=componente_curricular, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('educacao:componente_curricular_list')
    else:
        form = ComponenteCurricularForm(instance=componente_curricular, user=request.user)
    return render(request, 'componente_curricular/componente_curricular_form.html', {'form': form})

@login_required
@required_nivel_administrador
def componente_curricular_delete(request, pk):
    componente_curricular = get_object_or_404(Componente_Curricular, pk=pk)
    if request.method == 'POST':
        componente_curricular.delete()
        return redirect('educacao:componente_curricular_list')
    return render(request, 'componente_curricular/componente_curricular_confirm_delete.html', {'componente_curricular': componente_curricular})


#NIVEL ENSINO
@login_required
@required_nivel_assistente_administrativo
def nivel_ensino_list(request):
    niveis = Nivel_Ensino.objects.all()
    return render(request, 'nivel_ensino/nivel_ensino_list.html', {'niveis': niveis})

@login_required
@required_nivel_assistente_administrativo
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
@required_nivel_administrador
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
@required_nivel_administrador
def nivel_ensino_delete(request, pk):
    nivel = get_object_or_404(Nivel_Ensino, pk=pk)
    if request.method == 'POST':
        nivel.delete()
        return redirect('educacao:nivel_ensino_list')
    return render(request, 'nivel_ensino/nivel_ensino_confirm_delete.html', {'nivel': nivel})

#AVALIAÇÕES
@login_required
@required_nivel_professor
def avaliacoes_list(request):
    avaliacoes = Avaliacoes.objects.all()
    return render(request, 'educacao/avaliacoes/avaliacoes_list.html', {'avaliacoes': avaliacoes})


@login_required
@required_nivel_assistente_administrativo
def avaliacoes_create(request):
    if request.method == 'POST':
        # Limpa o nome do arquivo, se houver arquivo
        if 'arquivo' in request.FILES:
            arquivo = request.FILES['arquivo']
            arquivo.name = sanitize_filename(arquivo.name)

        form = AvaliacoesForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('educacao:tipo_avaliacoes_list')
    else:
        form = AvaliacoesForm(user=request.user)
    return render(request, 'educacao/avaliacoes/avaliacoes_form.html', {'form': form})

@login_required
@required_nivel_administrador
def avaliacoes_update(request, pk):
    avaliacao = get_object_or_404(Avaliacoes, pk=pk)
    if request.method == 'POST':
        if 'arquivo' in request.FILES:
            arquivo = request.FILES['arquivo']
            arquivo.name = sanitize_filename(arquivo.name)

        form = AvaliacoesForm(request.POST, request.FILES, instance=avaliacao, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('educacao:avaliacoes_list_educacao', ensino_id=avaliacao.nivel_ensino.id)
    else:
        form = AvaliacoesForm(instance=avaliacao, user=request.user)
    return render(request, 'educacao/avaliacoes/avaliacoes_form.html', {'form': form, 'avaliacao': avaliacao})

@login_required
@required_nivel_administrador
def avaliacoes_delete(request, pk):
    avaliacao = get_object_or_404(Avaliacoes, pk=pk)
    if request.method == 'POST':
        avaliacao.delete()
        return redirect('educacao:avaliacoes_list_educacao', ensino_id=avaliacao.nivel_ensino.id)

    return render(request, 'educacao/avaliacoes/avaliacoes_confirm_delete.html', {'avaliacao': avaliacao})



#TURMAS
@login_required
@required_nivel_professor
def turmas_list(request):
    turmas = Turmas.objects.all()
    return render(request, 'educacao/turmas/turmas_list.html', {'turmas': turmas})

@login_required
@required_nivel_professor
def escola_list_turmas(request, escola_id):
    escola = get_object_or_404(Escolas, pk=escola_id)
    turmas = Turmas.objects.filter(escola=escola)
    return render(request, 'educacao/turmas/turmas_list.html', {'turmas': turmas, 'escola': escola})


@login_required
@required_nivel_professor
def turma(request, turma_id):
    turma = get_object_or_404(Turmas, pk=turma_id)
    resultado_avaliacoes = Resultado_Avaliacoes.objects.filter(aluno_turma__turma=turma)
    return render(request, 'educacao/turmas/turma.html', {'turma': turma, 'resultado_avaliacoes': resultado_avaliacoes})


@login_required
@required_nivel_professor
def turmas_create(request):
    if request.method == 'POST':
        form = TurmasForm(request.POST, user=request.user)
        if form.is_valid():
            turma = form.save()  
            return redirect('educacao:turma', turma_id=turma.id)
    else:
        form = TurmasForm(user=request.user)
    return render(request, 'educacao/turmas/turmas_form.html', {'form': form})

@login_required
@required_nivel_diretor
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
@required_nivel_diretor
def turmas_delete(request, pk):
    turma = get_object_or_404(Turmas, pk=pk)
    if request.method == 'POST':
        turma.delete()
        return redirect('educacao:index')
    return render(request, 'educacao/turmas/turmas_confirm_delete.html', {'turma': turma})


#ALUNOS
@login_required
@required_nivel_professor
def alunos_create(request, turma_id):
    turma = get_object_or_404(Turmas, pk=turma_id)
    
    if request.method == 'POST':
        form_aluno = AlunosForm(request.POST)
        form_vinculo = AlunosTurmasForm(request.POST)
        form_resultado = ResultadoAvaliacoesForm(request.POST)
        form_observacao = ObservacoesAlunoForm(request.POST)

        if form_aluno.is_valid() and form_vinculo.is_valid() and form_resultado.is_valid() and form_observacao.is_valid():

            aluno = form_aluno.save(commit=False)
            aluno.user_inclusao = request.user
            aluno.save()

            observacao = form_observacao.save(commit=False)
            observacao.aluno = aluno
            observacao.user_inclusao = request.user
            observacao.save()
            
            vinculo = form_vinculo.save(commit=False)
            vinculo.aluno = aluno 
            vinculo.turma = turma
            vinculo.save()

            resultado = form_resultado.save(commit=False)
            resultado.user_inclusao = request.user
            resultado.aluno_turma = vinculo 

            if resultado.avaliacao1 or resultado.avaliacao2 or resultado.avaliacao3 or resultado.avaliacao4:
                resultado.verificar_capacitado()
            
            resultado.calcular_media()


            return redirect('educacao:turma', turma_id=turma.id)
    else:
        form_aluno = AlunosForm(initial={'user_inclusao': request.user})
        form_observacao = ObservacoesAlunoForm(initial={'user_inclusao': request.user})
        form_vinculo = AlunosTurmasForm(initial={'user_inclusao': request.user})
        form_resultado = ResultadoAvaliacoesForm()


    return render(request, 'educacao/alunos/alunos_form.html', {
        'form_aluno': form_aluno, 
        'form_vinculo': form_vinculo,
        'form_resultado': form_resultado,
        'form_observacao': form_observacao,
        'turma': turma
    })


@login_required
@required_nivel_professor
def alunos_update(request, pk, turma_id):
    aluno = get_object_or_404(Alunos, pk=pk, vinculos__turma=turma_id)
    turma = get_object_or_404(Turmas, pk=turma_id)
    vinculo = get_object_or_404(Aluno_Turma, aluno=aluno, turma=turma)
    resultado = get_object_or_404(Resultado_Avaliacoes, aluno_turma=vinculo)
    observacao = get_object_or_404(Observacoes_Aluno, aluno=aluno)

    if request.method == 'POST':

        form_aluno = AlunosForm(request.POST, instance=aluno)
        form_vinculo = AlunosTurmasForm(request.POST, instance=vinculo)
        form_resultado = ResultadoAvaliacoesForm(request.POST, instance=resultado)
        form_observacao = ObservacoesAlunoForm(request.POST, instance=observacao)

        if form_aluno.is_valid() and form_vinculo.is_valid() and form_resultado.is_valid() and form_observacao.is_valid():
            
            aluno = form_aluno.save(commit=False)
            aluno.user_edicao = request.user
            aluno.save()

            observacao = form_observacao.save(commit=False)
            observacao.aluno = aluno
            observacao.save()

            vinculo = form_vinculo.save(commit=False)
            vinculo.aluno = aluno
            vinculo.save()

            resultado = form_resultado.save(commit=False)
            resultado.aluno_turma = vinculo
            if resultado.avaliacao1 or resultado.avaliacao2 or resultado.avaliacao3 or resultado.avaliacao4:
                resultado.verificar_capacitado()
            
            resultado.calcular_media()

            return redirect('educacao:turma', turma_id=turma.id)
    else:
        form_aluno = AlunosForm(instance=aluno)
        form_observacao = ObservacoesAlunoForm(instance=observacao)
        form_vinculo = AlunosTurmasForm(instance=vinculo)
        form_resultado = ResultadoAvaliacoesForm(instance=resultado)

    return render(request, 'educacao/alunos/alunos_form.html', {
        'form_aluno': form_aluno, 
        'form_observacao': form_observacao,
        'form_vinculo': form_vinculo , 
        'form_resultado': form_resultado,
        'turma': turma,
        
    })



@login_required
@required_nivel_professor
def alunos_detalhe(request, pk, turma_id):
    turma = get_object_or_404(Turmas, pk=turma_id)
    aluno = get_object_or_404(Alunos, pk=pk, vinculos__turma=turma_id)
    vinculo = get_object_or_404(Aluno_Turma, aluno=aluno, turma=turma)
    resultado = get_object_or_404(Resultado_Avaliacoes, aluno_turma=vinculo)
    observacao = get_object_or_404(Observacoes_Aluno, aluno=aluno)

    return render(request, 'educacao/alunos/alunos_detalhe.html', {
        'observacao': observacao, 
        'turma': turma,
        'resultado': resultado,
    })



@login_required
@required_nivel_diretor
def alunos_delete(request, pk, turma_id):
    aluno = get_object_or_404(Alunos, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('educacao:turma', turma_id=turma_id)
    return render(request, 'educacao/alunos/alunos_confirm_delete.html', {'aluno': aluno, 'turma_id': turma_id})

#VIEWS QUE NÃO DEVERIAM EXISTIR

@login_required
@required_nivel_assistente_administrativo
def turmas_list_escola(request, id):
    escola = Escolas.objects.get(id=id)
    turmas_selected = Turmas.objects.filter(escola__id=escola)
    return render(request, 'educacao/turmas/turmas_list_educacao.html', {'turmas': turmas_selected})

@login_required
@required_nivel_professor
def avaliacoes_list_educacao(request, ensino_id):
    nivel_ensino = Nivel_Ensino.objects.get(id=ensino_id)
    avaliacoes_selected = Avaliacoes.objects.filter(nivel_ensino=nivel_ensino)
    return render(request, 'educacao/avaliacoes/avaliacao_list_educacao.html', {'avaliacoes': avaliacoes_selected})





#############################   Funções   #######################################

def sanitize_filename(filename):
    return unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode('ASCII')


