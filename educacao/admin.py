from django.contrib import admin
from .models import Tipo_Avaliacoes, Escolas, Nivel_Ensino, Avaliacoes, Turmas, Alunos, Componente_Curricular,  Aluno_Turma, Resultado_Avaliacoes, Observacoes_Aluno



@admin.register(Componente_Curricular)
class ComponenteCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dt_inclusao', 'user_inclusao')
    search_fields = ('nome',)
    list_filter = ('dt_inclusao',)

@admin.register(Tipo_Avaliacoes)
class TipoAvaliacoesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'componente_curricular', 'dt_inclusao', 'user_inclusao')
    search_fields = ('nome',)
    list_filter = ('dt_inclusao',)

@admin.register(Escolas)
class EscolasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'diretor', 'dt_inclusao', 'user_inclusao')
    search_fields = ('nome', 'diretor__nome')
    list_filter = ('dt_inclusao',)

@admin.register(Nivel_Ensino)
class NivelEnsinoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dt_inclusao', 'user_inclusao')
    search_fields = ('nome',)
    list_filter = ('dt_inclusao',)

@admin.register(Avaliacoes)
class AvaliacoesAdmin(admin.ModelAdmin):
    list_display = ('tipo_avaliacao', 'ano', 'semestre', 'nivel_ensino', 'arquivo', 'dt_inclusao', 'user_inclusao')
    search_fields = ('tipo_avaliacao__nome', 'ano', 'semestre')
    list_filter = ('ano', 'semestre', 'nivel_ensino')

@admin.register(Turmas)
class TurmasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'escola', 'nivel_ensino', 'dt_inclusao', 'user_inclusao')
    search_fields = ('nome', 'escola__nome', 'nivel_ensino__nome')
    list_filter = ('ano', 'escola', 'nivel_ensino')

@admin.register(Alunos)
class AlunosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dt_inclusao', 'user_inclusao')
    search_fields = ('nome',)
    list_filter = ('dt_inclusao',)
    
@admin.register(Aluno_Turma)
class AlunosTurmasAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'turma', 'status')
    search_fields = ('aluno__nome', 'turma__nome')
    list_filter = ('status', 'turma')

@admin.register(Resultado_Avaliacoes)
class ResultadoAvaliacoesAdmin(admin.ModelAdmin):
    list_display = ('aluno_nome', 'turma_nome', 'media_final', 'data')
    search_fields = ('aluno_turma__aluno__nome',)
    list_filter = ('data',)

    def aluno_nome(self, obj):
        return obj.aluno_turma.aluno.nome
    aluno_nome.short_description = 'Aluno'

    def turma_nome(self, obj):
        return obj.aluno_turma.turma.nome
    turma_nome.short_description = 'Turma'

@admin.register(Observacoes_Aluno)
class ObservacoesAlunoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'tipo')
    search_fields = ('aluno__nome',)
    list_filter = ('tipo',)
