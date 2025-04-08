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
    path('administrador_cadastro/', views.administrador_cadastro, name='administrador_cadastro'),
    path('diretor/', views.diretor_listar, name='diretor'),
    path('professor/', views.professor_listar, name='professor'),
    path('assistente_administrativo/', views.assistente_administrativo_listar, name='assistente_administrativo'),
    path('assistente_administrativo_cadastro/', views.assistente_administrativo_cadastro, name='assistente_administrativo_cadastro'),



    
]