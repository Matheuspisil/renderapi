from django import forms
from GPC.forms.forms import *
from GPC.models.mentor import Mentor

class CadastroMentor(forms.ModelForm):
    data_de_nascimento = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y'],
        label='Data de Nascimento'
    )

    class Meta:
        model = Mentor
        fields = ['cpf', 'data_de_nascimento', 'sexo', 'telefone', 'endereco', 'numero',
                  'complemento', 'bairro', 'cidade', 'estado', 'cep', 'profissao',
                  'experiencia_profissional', 'site', 'area_mentoria']
        widgets = {
            'senha': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CadastroMentor, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

#update do mentor
class MentorUpdateForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ['telefone', 'profissao', 'experiencia_profissional', 'profissao', 'site', 'area_mentoria', 
                  'cep', 'endereco', 'numero', 'bairro', 'cidade', 'complemento', 'estado']
