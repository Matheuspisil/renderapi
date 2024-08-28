from django import forms
from GPC.forms.forms import *
from GPC.models.vagas import Vaga
from datetime import date, timedelta


class VagaForm(forms.ModelForm):
    data_encerramento = forms.DateField(
        label='Data de Encerramento', widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
    )

    # Campos de autoconhecimento desejáveis
    etica = forms.BooleanField(label='Ética', required=False)
    autoeficacia = forms.BooleanField(label='Autoeficácia', required=False)
    trabalho_equipe = forms.BooleanField(
        label='Trabalho em Equipe', required=False)
    pens_criativo = forms.BooleanField(
        label='Pensamento Criativo', required=False)
    pens_analitico = forms.BooleanField(
        label='Pensamento Analítico', required=False)
    res_problemas = forms.BooleanField(
        label='Resolução de Problemas', required=False)
    comunicacao = forms.BooleanField(label='Comunicação', required=False)
    adaptabilidade = forms.BooleanField(label='Adaptabilidade', required=False)
    persistencia = forms.BooleanField(label='Persistência', required=False)
    agilidade = forms.BooleanField(label='Agilidade', required=False)
    gestao = forms.BooleanField(label='Gestão', required=False)
    orient_cliente = forms.BooleanField(
        label='Orientação ao Cliente', required=False)
    linguagens = forms.BooleanField(label='Linguagens', required=False)
    programacao = forms.BooleanField(label='Programação', required=False)
    ia = forms.BooleanField(label='Inteligência Artificial', required=False)
    bigdata = forms.BooleanField(label='Big Data', required=False)
    ciberseg = forms.BooleanField(label='Cibersegurança', required=False)
    redes = forms.BooleanField(label='Redes', required=False)
    qualidade = forms.BooleanField(label='Qualidade', required=False)

    class Meta:
        model = Vaga
        fields = ['empresa', 'titulo', 'descricao',
                  'requisitos', 'data_encerramento', 'ativo', 'tipo_vaga']
        exclude = ['empresa']
        widgets = {
            'data_encerramento': forms.DateInput(attrs={
                'type': 'date',
                'min': '2024-01-01',  # Defina aqui a data mínima desejada
                'max': '2025-12-31'   # Defina aqui a data máxima desejada
            }),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Salvar os campos de autoconhecimento desejáveis
        instance.etica = self.cleaned_data.get('etica', False)
        instance.autoeficacia = self.cleaned_data.get('autoeficacia', False)
        instance.trabalho_equipe = self.cleaned_data.get(
            'trabalho_equipe', False)
        instance.pens_criativo = self.cleaned_data.get('pens_criativo', False)
        instance.pens_analitico = self.cleaned_data.get(
            'pens_analitico', False)
        instance.res_problemas = self.cleaned_data.get('res_problemas', False)
        instance.comunicacao = self.cleaned_data.get('comunicacao', False)
        instance.adaptabilidade = self.cleaned_data.get(
            'adaptabilidade', False)
        instance.persistencia = self.cleaned_data.get('persistencia', False)
        instance.agilidade = self.cleaned_data.get('agilidade', False)
        instance.gestao = self.cleaned_data.get('gestao', False)
        instance.orient_cliente = self.cleaned_data.get(
            'orient_cliente', False)
        instance.linguagens = self.cleaned_data.get('linguagens', False)
        instance.programacao = self.cleaned_data.get('programacao', False)
        instance.ia = self.cleaned_data.get('ia', False)
        instance.bigdata = self.cleaned_data.get('bigdata', False)
        instance.ciberseg = self.cleaned_data.get('ciberseg', False)
        instance.redes = self.cleaned_data.get('redes', False)
        instance.qualidade = self.cleaned_data.get('qualidade', False)

        if commit:
            instance.save()
        return instance


class UpdateVagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['titulo', 'descricao', 'requisitos',
                  'data_encerramento', 'ativo']
