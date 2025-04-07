from django.contrib import admin
from .models import Pessoa, Administrador, Assistente_Administrativo, Diretor, Professor


# Register your models here.
admin.site.register(Pessoa) 
admin.site.register(Administrador)
admin.site.register(Assistente_Administrativo)
admin.site.register(Diretor)
admin.site.register(Professor)