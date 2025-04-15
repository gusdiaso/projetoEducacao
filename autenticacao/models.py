# import User7
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Pessoa(models.Model):
    TIPO_CONTA_CHOICES = (
        ('adm', 'Administrador'),
        ('ass', 'Assistente Administrativo'),
        ('dir', 'Diretor'),
        ('pro', 'Professor')

    )   
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pessoa_user', null=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    tipo_conta = models.CharField(max_length=3, choices=TIPO_CONTA_CHOICES)

    user_inclusao = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='pessoa_user_inclusao', null=True)
    dt_inlusao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome


    def is_professor(self):
        return self.tipo_conta == 'pro'