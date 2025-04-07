# import User7
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pessoa')
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Administrador(Pessoa):

    def __str__(self):
        return self.nome

class Assistente_Administrativo(Pessoa):

    def __str__(self):
        return self.nome    

class Diretor(Pessoa):

    def __str__(self):
        return self.nome
    
class Professor(Pessoa):
    disciplina = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    

    