from django import forms
from GPC.forms.forms import *
from GPC.models.empresa import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['cnpj', 'razao_social', 'endereco', 'numero', 'complemento',
                  'bairro', 'cidade', 'estado', 'cep', 'telefone', 'site', 'ativo']
        widgets = {
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmpresaForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class EmpresaUpdateForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['telefone', 'site', 'ativo', 'endereco', 'numero',
                  'complemento', 'bairro', 'cidade', 'estado', 'cep',]