from django import forms
from GPC.forms.forms import *
from GPC.models.aluno import Aluno
from datetime import date


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['matricula', 'cpf', 'data_de_nascimento', 'sexo', 'telefone',
                  'endereco', 'numero', 'complemento', 'bairro', 'cidade',
                  'estado', 'cep', 'curso', 'semestre']

        today = date.today()
        min_year = today.year - 100

        widgets = {
            'data_de_nascimento': forms.DateInput(attrs={
                'type': 'date',
                'max': today.strftime('%Y-%m-%d'),
                'min': date(min_year, today.month, today.day).strftime('%Y-%m-%d')
            }),
            'cpf': forms.TextInput(attrs={'placeholder': 'somente números'})
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not cpf.isdigit():
            raise forms.ValidationError("O CPF deve conter apenas números.")
        if len(cpf) != 11:
            raise forms.ValidationError(
                "O CPF deve conter exatamente 11 dígitos.")
        return cpf


class AlunoUpdateForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['telefone', 'semestre', 'endereco', 'numero',
                  'complemento', 'bairro', 'cidade', 'estado', 'cep',]
