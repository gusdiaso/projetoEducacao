from django import forms
from .models import Tipo_Avaliacoes
from .models import Escolas
from .models import Nivel_Ensino
from .models import Avaliacoes
from .models import Turmas, Alunos

class TipoAvaliacoesForm(forms.ModelForm):
    user_inclusao = forms.ModelChoiceField(
        queryset=None, widget=forms.HiddenInput(), required=False
    )
    user_edicao = forms.ModelChoiceField(
        queryset=None, widget=forms.HiddenInput(), required=False
    )

    class Meta:
        model = Tipo_Avaliacoes
        fields = ['nome', 'arquivo', 'user_inclusao', 'user_edicao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
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

class EscolasForm(forms.ModelForm):
    user_inclusao = forms.ModelChoiceField(
        queryset=None, widget=forms.HiddenInput(), required=False
    )
    user_edicao = forms.ModelChoiceField(
        queryset=None, widget=forms.HiddenInput(), required=False
    )

    class Meta:
        model = Escolas
        fields = ['nome', 'diretor', 'user_inclusao', 'user_edicao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'diretor': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user_inclusao'].initial = user
            self.fields['user_edicao'].initial = user
            self.fields['user_inclusao'].queryset = user.__class__.objects.filter(pk=user.pk)
            self.fields['user_edicao'].queryset = user.__class__.objects.filter(pk=user.pk)
        # Filtrar apenas pessoas com tipo_conta='dir' para o campo diretor
        self.fields['diretor'].queryset = self.fields['diretor'].queryset.filter(tipo_conta='dir')

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
        fields = ['tipo_avaliacao', 'ano', 'semestre', 'nivel_ensino', 'user_inclusao', 'user_edicao']
        widgets = {
            'tipo_avaliacao': forms.Select(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'semestre': forms.NumberInput(attrs={'class': 'form-control'}),
            'nivel_ensino': forms.Select(attrs={'class': 'form-control'}),
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
    user_inclusao = forms.ModelChoiceField(
        queryset=None, widget=forms.HiddenInput(), required=False
    )
    user_edicao = forms.ModelChoiceField(
        queryset=None, widget=forms.HiddenInput(), required=False
    )

    class Meta:
        model = Turmas
        fields = ['nome', 'ano', 'escola', 'nivel_ensino', 'user_inclusao', 'user_edicao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'escola': forms.Select(attrs={'class': 'form-control'}),
            'nivel_ensino': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user_inclusao'].initial = user
            self.fields['user_edicao'].initial = user
            self.fields['user_inclusao'].queryset = user.__class__.objects.filter(pk=user.pk)
            self.fields['user_edicao'].queryset = user.__class__.objects.filter(pk=user.pk)

class AlunosForm(forms.ModelForm):
    user_inclusao = forms.ModelChoiceField(
        queryset=None, widget=forms.HiddenInput(), required=False
    )
    user_edicao = forms.ModelChoiceField(
        queryset=None, widget=forms.HiddenInput(), required=False
    )

    class Meta:
        model = Alunos
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
