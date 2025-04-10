from django.contrib import admin
from .models import Pessoa
@admin.register(Pessoa)

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email', 'tipo_conta')  # Adjust fields as per your model
    search_fields = ('nome', 'email', 'cpf')      # Adjust fields as per your model
    list_filter = ('tipo_conta',)        # Adjust fields as per your model