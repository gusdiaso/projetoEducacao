from django.db import models
from autenticacao.models import Pessoa, User

class BaseModel(models.Model):
    dt_inclusao = models.DateTimeField(auto_now_add=True)
    user_inclusao = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_inclusao")
    dt_edicao = models.DateTimeField(auto_now=True)
    user_edicao = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_edicao", null=True, blank=True)

    class Meta:
        abstract = True

    def get_pessoa_inclusao(self):
        return Pessoa.objects.filter(user=self.user_inclusao).first()

class Tipo_Avaliacoes(BaseModel):
    nome = models.CharField(max_length=100)        
    arquivo = models.FileField(upload_to='avaliacoes/')

    def __str__(self):
        return f"Avaliação {self.nome}"

class Escolas(BaseModel):
    nome = models.CharField(max_length=100)        
    diretor = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='escolas_diretor')

    def __str__(self):
        return f"Escola {self.nome}"
    
    def save(self, *args, **kwargs):
        if self.diretor.tipo_conta != 'dir':
            raise ValueError("Apenas pessoas com tipo_conta igual a 'dir' podem ser diretores.")
        super().save(*args, **kwargs)

class Nivel_Ensino(BaseModel):
    nome = models.CharField(max_length=100)            

    def __str__(self):
        return f"Nível de Ensino {self.nome}"
    
    def get_turmas(self, user):
        turmas = Turmas.objects.filter(nivel_ensino=self, professor__user=user)
        return turmas
    
class Avaliacoes(BaseModel):
    tipo_avaliacao = models.ForeignKey(Tipo_Avaliacoes, on_delete=models.CASCADE, related_name='avaliacoes')
    ano = models.IntegerField(verbose_name="Ano de realização da avaliação")
    semestre = models.IntegerField(verbose_name="Semestre de realização da avaliação")
    nivel_ensino = models.ForeignKey(Nivel_Ensino, on_delete=models.CASCADE, related_name='avaliacoes')

#
class Turmas(BaseModel):
    professor = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='turmas_professor', null=True)
    nome = models.CharField(max_length=100)        
    ano = models.IntegerField(verbose_name="Ano de atuação da turma")
    escola = models.ForeignKey(Escolas, on_delete=models.CASCADE, related_name='turmas')    
    nivel_ensino = models.ForeignKey(Nivel_Ensino, on_delete=models.CASCADE, related_name='turmas')

    def __str__(self):
        return f"Turma {self.nome} - {self.ano}"

class Alunos(BaseModel):
    nome = models.CharField(max_length=100)        
    turma = models.ForeignKey(Turmas, on_delete=models.CASCADE, related_name='alunos')

    def get_escola(self):
        return self.turma.escola.nome

    get_escola.short_description = "Escola"

# class Resultado_Avaliacoes