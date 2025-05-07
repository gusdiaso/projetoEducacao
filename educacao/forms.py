from django import forms
from autenticacao.models import Pessoa
from .models import Tipo_Avaliacoes
from .models import Escolas
from .models import Nivel_Ensino
from .models import Avaliacoes
from .models import Turmas, Alunos
from .models import Componente_Curricular
from .models import Aluno_Turma
from .models import Resultado_Avaliacoes
from .models import Observacoes_Aluno


class TipoAvaliacoesForm(forms.ModelForm):
    class Meta:
        model = Tipo_Avaliacoes
        fields = ['nome', 'componente_curricular', 'user_inclusao', 'user_edicao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'componente_curricular': forms.Select(attrs={'class': 'form-control'}),
            'user_inclusao': forms.HiddenInput(),
            'user_edicao': forms.HiddenInput(),
        }


class ComponenteCurricularForm(forms.ModelForm):
    user_inclusao = forms.ModelChoiceField(
        queryset=None, widget=forms.HiddenInput(), required=False
    )
    user_edicao = forms.ModelChoiceField(
        queryset=None, widget=forms.HiddenInput(), required=False
    )

    class Meta:
        model = Componente_Curricular
        fields = ['nome', 'user_inclusao', 'user_edicao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user_inclusao'].initial = user
            self.fields['user_edicao'].initial = user
            self.fields['user_inclusao'].queryset = user.__class__.objects.filter(pk=user.pk)
            self.fields['user_edicao'].queryset = user.__class__.objects.filter(pk=user.pk)


class EscolasForm(forms.ModelForm):
    class Meta:
        model = Escolas
        fields = ['nome', 'diretor', 'professor', 'user_inclusao', 'user_edicao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'diretor': forms.Select(attrs={'class': 'form-control'}),
            'professor': forms.Select(attrs={'class': 'form-control'}),
            'user_inclusao': forms.HiddenInput(),
            'user_edicao': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        if user:
            user_inclusao = forms.ModelChoiceField(
                queryset=None, widget=forms.HiddenInput(), required=False
            )
            user_edicao = forms.ModelChoiceField(
                queryset=None, widget=forms.HiddenInput(), required=False
            )

        super().__init__(*args, **kwargs)
        if user:
            print(user.id)
            self.fields['user_inclusao'].initial = user.id
            self.fields['user_edicao'].initial = user.id
            self.fields['user_inclusao'].queryset = user.__class__.objects.filter(pk=user.pk)
            self.fields['user_edicao'].queryset = user.__class__.objects.filter(pk=user.pk)
        # Filtrar apenas pessoas com tipo_conta='dir' para o campo diretor
        self.fields['diretor'].queryset = self.fields['diretor'].queryset.filter(tipo_conta='dir')
        self.fields['professor'].queryset = self.fields['professor'].queryset.filter(tipo_conta='pro')


class EscolasEditForm(forms.ModelForm):
    class Meta:
        model = Escolas
        fields = ['nome', 'diretor', 'professor', 'user_inclusao', 'user_edicao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'diretor': forms.Select(attrs={'class': 'form-control'}),
            'professor': forms.Select(attrs={'class': 'form-control'}),
            'user_inclusao': forms.HiddenInput(),
            'user_edicao': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        if user:
            user_inclusao = forms.ModelChoiceField(
                queryset=None, widget=forms.HiddenInput(), required=False
            )
            user_edicao = forms.ModelChoiceField(
                queryset=None, widget=forms.HiddenInput(), required=False
            )

        super().__init__(*args, **kwargs)
        if user:
            self.fields['user_inclusao'].initial = user.id
            self.fields['user_edicao'].initial = user.id
            self.fields['user_inclusao'].queryset = user.__class__.objects.filter(pk=user.pk)
            self.fields['user_edicao'].queryset = user.__class__.objects.filter(pk=user.pk)
        # Filtrar apenas pessoas com tipo_conta='dir' para o campo diretor
        self.fields['diretor'].queryset = self.fields['diretor'].queryset.filter(tipo_conta='dir')
        self.fields['professor'].queryset = self.fields['professor'].queryset.filter(tipo_conta='pro')


class NivelEnsinoForm(forms.ModelForm):
    user_inclusao = forms.ModelChoiceField(
        queryset=None, widget=forms.HiddenInput(), required=False
    )
    user_edicao = forms.ModelChoiceField(
        queryset=None, widget=forms.HiddenInput(), required=False
    )

    class Meta:
        model = Nivel_Ensino
        fields = ['nome', 'user_inclusao', 'user_edicao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user_inclusao'].initial = user
            self.fields['user_edicao'].initial = user
            self.fields['user_inclusao'].queryset = user.__class__.objects.filter(pk=user.pk)
            self.fields['user_edicao'].queryset = user.__class__.objects.filter(pk=user.pk)


class AvaliacoesForm(forms.ModelForm):
    user_inclusao = forms.ModelChoiceField(
        queryset=None, widget=forms.HiddenInput(), required=False
    )
    user_edicao = forms.ModelChoiceField(
        queryset=None, widget=forms.HiddenInput(), required=False
    )

    class Meta:
        model = Avaliacoes
        fields = ['tipo_avaliacao', 'ano', 'semestre', 'nivel_ensino', 'arquivo', 'user_inclusao', 'user_edicao']
        widgets = {
            'tipo_avaliacao': forms.Select(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'semestre': forms.NumberInput(attrs={'class': 'form-control'}),
            'nivel_ensino': forms.Select(attrs={'class': 'form-control'}),
            'arquivo': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user_inclusao'].initial = user
            self.fields['user_edicao'].initial = user
            self.fields['user_inclusao'].queryset = user.__class__.objects.filter(pk=user.pk)
            self.fields['user_edicao'].queryset = user.__class__.objects.filter(pk=user.pk)


class TurmasForm(forms.ModelForm):
    class Meta:
        model = Turmas
        fields = ['nome', 'ano', 'escola', 'nivel_ensino', 'user_inclusao', 'user_edicao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'escola': forms.Select(attrs={'class': 'form-control'}),
            'nivel_ensino': forms.Select(attrs={'class': 'form-control'}),
            'user_inclusao': forms.HiddenInput(),
            'user_edicao': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user_inclusao'].initial = user.pk
            self.fields['user_edicao'].initial = user.pk


class AlunosForm(forms.ModelForm):

    class Meta:
        model = Alunos
        fields = ['nome', 'user_inclusao', 'user_edicao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'user_inclusao': forms.HiddenInput(),
            'user_edicao': forms.HiddenInput(),
        }

class AlunosEditForm(forms.ModelForm):
    class Meta:
        model = Alunos
        fields = ['nome', 'user_inclusao', 'user_edicao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'user_inclusao': forms.HiddenInput(),
            'user_edicao': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user_inclusao'].initial = user.pk
            self.fields['user_edicao'].initial = user.pk



class ResultadoAvaliacoesForm(forms.ModelForm):
    class Meta:
        model = Resultado_Avaliacoes
        fields = ['aluno_turma', 'avaliacao1', 'tipo_avaliacao1', 'avaliacao2', 'tipo_avaliacao2', 'avaliacao3', 'tipo_avaliacao3', 'avaliacao4', 'tipo_avaliacao4', 'media_final']
        exclude = ['aluno_turma']  

        widgets = {
            'aluno_turma': forms.Select(attrs={'class': 'form-control'}),
            'avaliacao1': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': 0, 'max': 10}),
            'tipo_avaliacao1': forms.Select(attrs={'class': 'form-control'}),
            'avaliacao2': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': 0, 'max': 10}),
            'tipo_avaliacao2': forms.Select(attrs={'class': 'form-control'}),
            'avaliacao3': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': 0, 'max': 10}),
            'tipo_avaliacao3': forms.Select(attrs={'class': 'form-control'}),
            'avaliacao4': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': 0, 'max': 10}),
            'tipo_avaliacao4': forms.Select(attrs={'class': 'form-control'}),
            'media_final': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }


class AlunosTurmasForm(forms.ModelForm):
    class Meta:
        model = Aluno_Turma
        fields = ['status', 'user_inclusao', 'user_edicao']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'user_inclusao': forms.HiddenInput(),
            'user_edicao': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user_inclusao'].initial = user.pk
            self.fields['user_edicao'].initial = user.pk


class ObservacoesAlunoForm(forms.ModelForm):
    class Meta:
        model = Observacoes_Aluno
        fields = ['tipo', 'descricao', 'user_inclusao', 'user_edicao']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'rows': 4}),
            'user_inclusao': forms.HiddenInput(),
            'user_edicao': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user_inclusao'].initial = user.pk
            self.fields['user_edicao'].initial = user.pk
