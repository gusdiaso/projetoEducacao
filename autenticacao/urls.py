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

    path('usuarios/', views.usuario_listar, name='usuarios'),
    path('usuario-adicionar/', views.usuario_adicionar, name='usuario_adicionar'),
    path('usuario-editar/<int:id>/', views.usuario_editar, name='usuario_editar'),
    path('usuario-toggle-ativo/<int:id>/', views.usuario_toggle_ativo, name='usuario_toggle_ativo'),
]