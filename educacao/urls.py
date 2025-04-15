from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'educacao'
urlpatterns = [
    path('', views.index, name='index'),
    # path('educacao/', include('educacao.urls')),,
    path('tipos-avaliacoes/', views.tipo_avaliacoes_list, name='tipo_avaliacoes_list'),
    path('tipos-avaliacoes/criar/', views.tipo_avaliacoes_create, name='tipo_avaliacoes_create'),
    path('tipos-avaliacoes/<int:pk>/atualizar/', views.tipo_avaliacoes_update, name='tipo_avaliacoes_update'),
    path('tipos-avaliacoes/<int:pk>/excluir/', views.tipo_avaliacoes_delete, name='tipo_avaliacoes_delete'),
    
    path('escolas/', views.escolas_list, name='escolas_list'),

    path('escolas_educacao/', views.escolas_list_educacao, name='escolas_list_educacao'),
    path('escolas/criar/', views.escolas_create, name='escolas_create'),
    path('escolas/<int:pk>/atualizar/', views.escolas_update, name='escolas_update'),
    path('escolas/<int:pk>/excluir/', views.escolas_delete, name='escolas_delete'),

    path('niveis-ensino/', views.nivel_ensino_list, name='nivel_ensino_list'),
    path('niveis-ensino/criar/', views.nivel_ensino_create, name='nivel_ensino_create'),
    path('niveis-ensino/<int:pk>/atualizar/', views.nivel_ensino_update, name='nivel_ensino_update'),
    path('niveis-ensino/<int:pk>/excluir/', views.nivel_ensino_delete, name='nivel_ensino_delete'),

    path('avaliacoes/', views.avaliacoes_list, name='avaliacoes_list'),
    path('avaliacoes/criar/', views.avaliacoes_create, name='avaliacoes_create'),
    path('avaliacoes/<int:pk>/atualizar/', views.avaliacoes_update, name='avaliacoes_update'),
    path('avaliacoes/<int:pk>/excluir/', views.avaliacoes_delete, name='avaliacoes_delete'),
    path('avaliacoes_educacao/<int:ensino_id>/', views.avaliacoes_list_educacao, name='avaliacoes_list_educacao'),
    path('avaliacoes/download/<int:avaliacao_id>/', views.avaliacao_download, name='avaliacoes_download'),

    path('turmas/', views.turmas_list, name='turmas_list'),
    path('turmas_educacao/<int:ensino_id>/', views.turmas_list_educacao, name='turmas_list_educacao'),
    path('turmas_escola/<int:ensino_id>/', views.turmas_list_escola, name='turmas_list_escola'),
    path('turmas/criar/', views.turmas_create, name='turmas_create'),
    path('turmas/<int:pk>/atualizar/', views.turmas_update, name='turmas_update'),
    path('turmas/<int:pk>/excluir/', views.turmas_delete, name='turmas_delete'),
    path('turmas/<int:turma_id>/alunos/', views.alunos_list, name='alunos_list'),
    path('turmas/<int:turma_id>/alunos/criar/', views.alunos_create, name='alunos_create'),
    path('turmas/<int:turma_id>/alunos/<int:pk>/excluir/', views.alunos_delete, name='alunos_delete'),
]
