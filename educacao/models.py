from django.db import models
from autenticacao.models import Pessoa, User
from django.core.validators import MinValueValidator, MaxValueValidator

class Base_Model(models.Model):
    dt_inclusao = models.DateTimeField(auto_now_add=True)
    user_inclusao = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_inclusao")
    dt_edicao = models.DateTimeField(auto_now=True)
    user_edicao = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_edicao", null=True, blank=True)

    class Meta:
        abstract = True

    def get_pessoa_inclusao(self):
        return Pessoa.objects.filter(user=self.user_inclusao).first()


class Componente_Curricular(Base_Model):
    nome = models.CharField(max_length=200)  

    def __str__(self):
        return self.nome


class Tipo_Avaliacoes(Base_Model):
    nome = models.CharField(max_length=100)  
    componente_curricular = models.ForeignKey(Componente_Curricular, on_delete=models.CASCADE, related_name='componente_curricular', null=True)

    def __str__(self):
        return f"{self.nome} ({self.componente_curricular})"


class Escolas(Base_Model):
    nome = models.CharField(max_length=100)        
    diretor = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='escolas_diretor')
    professor = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='escolas_professor', null=True)

    def __str__(self):
        return f"{self.nome}"
    
    def save(self, *args, **kwargs):
        if self.diretor.tipo_conta != 'dir':
            raise ValueError("Apenas pessoas com tipo_conta igual a 'dir' podem ser diretores.")
        super().save(*args, **kwargs)


class Nivel_Ensino(Base_Model):
    nome = models.CharField(max_length=100)            
    class Meta:
        ordering = ['nome'] 

    def __str__(self):
        return f"Nível de Ensino {self.nome}"
    
    def get_turmas(self, user):
        turmas = Turmas.objects.filter(nivel_ensino=self, escola__professor__user=user)
        return turmas

class Avaliacoes(Base_Model):
    tipo_avaliacao = models.ForeignKey(Tipo_Avaliacoes, on_delete=models.CASCADE, related_name='avaliacoes')
    ano = models.IntegerField(verbose_name="Ano de realização da avaliação")
    semestre = models.IntegerField(verbose_name="Semestre de realização da avaliação")
    nivel_ensino = models.ForeignKey(Nivel_Ensino, on_delete=models.CASCADE, related_name='avaliacoes')
    arquivo = models.FileField(upload_to='caminho/desejado/', null=True)

    def __str__(self):
        return f"{self.tipo_avaliacao.nome} ({self.tipo_avaliacao.componente_curricular} - {self.ano}.{self.semestre})"


class Turmas(Base_Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField(verbose_name="Ano de atuação da turma")
    escola = models.ForeignKey('Escolas', on_delete=models.CASCADE, related_name='turmas')
    nivel_ensino = models.ForeignKey('Nivel_Ensino', on_delete=models.CASCADE, related_name='turmas')

    class Meta:
        ordering = ['-ano', 'nome']

    def __str__(self):
        return f"Turma {self.nome} ({self.ano})"

    def total_alunos(self):
        return self.alunos_turma.count()

    total_alunos.short_description = "Qtd. Alunos"


class Alunos(Base_Model):
    nome = models.CharField(max_length=100)
    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_escola(self):
        # Pega a escola da última turma que ele participou
        ultimo_vinculo = self.vinculos.order_by('-ano_letivo').first()
        return ultimo_vinculo.turma.escola.nome if ultimo_vinculo else "Sem escola vinculada"

    get_escola.short_description = "Escola"


class Aluno_Turma(Base_Model):
    aluno = models.ForeignKey('Alunos', on_delete=models.CASCADE, related_name='vinculos')
    turma = models.ForeignKey('Turmas', on_delete=models.CASCADE, related_name='alunos_turma')
    status = models.CharField(
        max_length=20,
        choices=[('matriculado', 'Matriculado'), ('aprovado', 'Aprovado'), ('reprovado', 'Reprovado'), ('transferido', 'Transferido')],
        default='matriculado'
    )

    def __str__(self):
        return f"{self.aluno.nome} - {self.turma.nome} ({self.turma.nivel_ensino})"


class Resultado_Avaliacoes(Base_Model):

    STATUS_CHOICES = [
        ('capacitado', 'Capacitado'),
        ('naocapacitado', 'Não Capacitado'),
    ]

    aluno_turma = models.ForeignKey('Aluno_Turma', on_delete=models.CASCADE, related_name='resultados')
    avaliacao1 = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, validators=[MinValueValidator(0.00), MaxValueValidator(10.00)],verbose_name="Nota da 1° avaliação")
    avaliacao2 = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, validators=[MinValueValidator(0.00), MaxValueValidator(10.00)], verbose_name="Nota da 2° avaliação")
    avaliacao3 = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, validators=[MinValueValidator(0.00), MaxValueValidator(10.00)], verbose_name="Nota da 3° avaliação")
    avaliacao4 = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, validators=[MinValueValidator(0.00), MaxValueValidator(10.00)], verbose_name="Nota da 4° avaliação")
    media_final = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, validators=[MinValueValidator(0.00), MaxValueValidator(10.00)], verbose_name="Média Final")
    
    tipo_avaliacao1 = models.ForeignKey('Avaliacoes', on_delete=models.SET_NULL, null=True, blank=True, related_name='tipo_avaliacao1')
    tipo_avaliacao2 = models.ForeignKey('Avaliacoes', on_delete=models.SET_NULL, null=True, blank=True, related_name='tipo_avaliacao2')
    tipo_avaliacao3 = models.ForeignKey('Avaliacoes', on_delete=models.SET_NULL, null=True, blank=True, related_name='tipo_avaliacao3')
    tipo_avaliacao4 = models.ForeignKey('Avaliacoes', on_delete=models.SET_NULL, null=True, blank=True, related_name='tipo_avaliacao4')

    status_avaliacao1 = models.CharField(max_length=13, choices=STATUS_CHOICES, null=True, editable=False)
    status_avaliacao2 = models.CharField(max_length=13, choices=STATUS_CHOICES, null=True, editable=False)
    status_avaliacao3 = models.CharField(max_length=13, choices=STATUS_CHOICES, null=True, editable=False)
    status_avaliacao4 = models.CharField(max_length=13, choices=STATUS_CHOICES, null=True, editable=False)

    
    data = models.DateField(auto_now_add=True)


    def calcular_media(self):
        """Método para calcular a média das avaliações"""
        avaliacoes = [self.avaliacao1, self.avaliacao2, self.avaliacao3, self.avaliacao4]
        self.media_final = sum(avaliacoes) / len(avaliacoes)
        self.aprovado = self.media_final >= 6.00  # Considerando que a média de aprovação é 6.00
        self.save()

    
    def verificar_capacitado(self):
        if self.avaliacao1 >= 6.00:
            self.status_avaliacao1 = 'capacitado'
        else:
            self.status_avaliacao1 = 'naocapacitado'

        if self.avaliacao2 >= 6.00:
            self.status_avaliacao2 = 'capacitado'
        else:
            self.status_avaliacao2 = 'naocapacitado'

        if self.avaliacao3 >= 6.00:
            self.status_avaliacao3 = 'capacitado'
        else:
            self.status_avaliacao3 = 'naocapacitado'
        
        if self.avaliacao4 >= 6.00:
            self.status_avaliacao4 = 'capacitado'
        else:
            self.status_avaliacao4 = 'naocapacitado'
        
        print(self.status_avaliacao1, self.status_avaliacao2, self.status_avaliacao3, self.status_avaliacao4)
        self.save()



    def __str__(self):
        return f"{self.tipo_avaliacoes} - {self.aluno_turma.aluno.nome} - {self.media_final}"

class Observacoes_Aluno(Base_Model):
    aluno = models.ForeignKey('Alunos', on_delete=models.CASCADE, related_name='observacoes')
    tipo = models.CharField(
        max_length=50,
        verbose_name="Tipo de Observação",
        choices=[('laudo', 'Laudo'), ('comportamento', 'Comportamento'), ('saude', 'Saúde'), ('outro', 'Outro')],
        default='outro'
    )
    descricao = models.CharField(max_length=1000, verbose_name='Descrição da Observação', default='Nenhuma observação registrada.')
    
    def __str__(self):
        return f"Obs: {self.tipo} - {self.aluno.nome}"






