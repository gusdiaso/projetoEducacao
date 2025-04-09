from django.urls import path
from . import views

app_name='autenticacao'
urlpatterns = [

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('passwd_reset/', views.passwd_reset, name='passwd_reset'),
    path('passwd_reset_confirm/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(), name='passwd_reset_confirm'),
    path('passwd_reset_done/', views.PasswordResetDoneView.as_view(), name='passwd_reset_done'),
    path('passwd_reset_complete/', views.PasswordResetCompleteView.as_view(), name='passwd_reset_complete'),

    path('painel_administrativo/', views.painel_administrativo, name='painel_administrativo'),

    path('administrador/', views.administrador_listar, name='administrador'),
    path('administrador_adicionar/', views.administrador_adicionar, name='administrador_adicionar'),
    path('administrador_editar/<int:id>/', views.administrador_editar, name='administrador_editar'),
    path('administrador_deletar/<int:id>/', views.administrador_deletar, name='administrador_deletar'),


    path('diretor/', views.diretor_listar, name='diretor'),
    path('diretor_adicionar/', views.diretor_adicionar, name='diretor_adicionar'),
    path('diretor_editar/<int:id>/', views.diretor_editar, name='diretor_editar'),
    path('diretor_deletar/<int:id>/', views.diretor_deletar, name='diretor_deletar'),
    
    path('professor/', views.professor_listar, name='professor'),
    
    path('assistente_administrativo/', views.assistente_administrativo_listar, name='assistente_administrativo'),
    path('assistente_administrativo_adicionar/', views.assistente_administrativo_adicionar, name='assistente_administrativo_adicionar'),
    path('assistente_administrativo_editar/<int:id>/', views.assistente_administrativo_editar, name='assistente_administrativo_editar'),
    path('assistente_administrativo_deletar/<int:id>/', views.assistente_administrativo_deletar, name='assistente_administrativo_deletar'),
]