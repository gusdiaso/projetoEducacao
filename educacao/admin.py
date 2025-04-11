from django.contrib import admin
from .models import Tipo_Avaliacoes, Escolas, Nivel_Ensino, Avaliacoes, Turmas, Alunos

@admin.register(Tipo_Avaliacoes)
class TipoAvaliacoesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'arquivo', 'dt_inclusao', 'user_inclusao')
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
    list_display = ('tipo_avaliacao', 'ano', 'semestre', 'nivel_ensino', 'dt_inclusao', 'user_inclusao')
    search_fields = ('tipo_avaliacao__nome', 'ano', 'semestre')
    list_filter = ('ano', 'semestre', 'nivel_ensino')

@admin.register(Turmas)
class TurmasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'escola', 'nivel_ensino', 'dt_inclusao', 'user_inclusao')
    search_fields = ('nome', 'escola__nome', 'nivel_ensino__nome')
    list_filter = ('ano', 'escola', 'nivel_ensino')

@admin.register(Alunos)
class AlunosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'get_escola', 'turma')
    list_filter = ('turma__escola',)
