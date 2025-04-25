from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'educacao'
urlpatterns = [
    path('', views.index, name='index'),

    #TIPO AVALIAÇÕES
    path('tipos-avaliacoes/', views.tipo_avaliacoes_list, name='tipo_avaliacoes_list'),
    path('tipos-avaliacoes/criar/', views.tipo_avaliacoes_create, name='tipo_avaliacoes_create'),
    path('tipos-avaliacoes/<int:pk>/editar/', views.tipo_avaliacoes_update, name='tipo_avaliacoes_update'),
    path('tipos-avaliacoes/<int:pk>/excluir/', views.tipo_avaliacoes_delete, name='tipo_avaliacoes_delete'),        

    
    #ESCOLAS
    path('escolas/', views.escolas_list, name='escolas_list'),
    path('escolas/criar/', views.escolas_create, name='escolas_create'),
    path('escolas/<int:pk>/editar/', views.escolas_update, name='escolas_update'),
    path('escolas/<int:pk>/excluir/', views.escolas_delete, name='escolas_delete'),
    path('escolas/turmas/<int:escola_id>/', views.escola_list_turmas, name='escola_list_turmas'),
        
    #Gerenciamento da Turma
    path('turmas/<int:turma_id>/', views.turma, name='turma'),
    path('turmas/<int:pk>/editar/', views.turmas_update, name='turmas_update'),
    path('turmas/', views.turmas_list, name='turmas_list'),
    path('turmas/<int:pk>/excluir/', views.turmas_delete, name='turmas_delete'),


    path('turmas/criar/', views.turmas_create, name='turmas_create'),
    #Gerenciamento dos alunos    
    path('turmas/<int:turma_id>/alunos/criar/', views.alunos_create, name='alunos_create'),
    path('turmas/<int:turma_id>/alunos/<int:pk>/excluir/', views.alunos_delete, name='alunos_delete'),
    
    #PAINEL ADMINISTRATIVO
    
    path('niveis-ensino/', views.nivel_ensino_list, name='nivel_ensino_list'),
    path('niveis-ensino/criar/', views.nivel_ensino_create, name='nivel_ensino_create'),
    path('niveis-ensino/<int:pk>/editar/', views.nivel_ensino_update, name='nivel_ensino_update'),
    path('niveis-ensino/<int:pk>/excluir/', views.nivel_ensino_delete, name='nivel_ensino_delete'),

    path('avaliacoes/<int:id>/download/', views.avaliacao_download, name='avaliacao_download'),
    path('avaliacoes/', views.avaliacoes_list, name='avaliacoes_list'),
    path('avaliacoes/criar/', views.avaliacoes_create, name='avaliacoes_create'),
    path('avaliacoes/<int:pk>/editar/', views.avaliacoes_update, name='avaliacoes_update'),
    path('avaliacoes/<int:pk>/excluir/', views.avaliacoes_delete, name='avaliacoes_delete'),

    
    
    #ROTAS QUE NÃO DEVERIAM EXISTIR
    path('escolas_educacao/', views.escolas_list_educacao, name='escolas_list_educacao'),
    path('avaliacoes_educacao/<int:ensino_id>/', views.avaliacoes_list_educacao, name='avaliacoes_list_educacao'),

]
