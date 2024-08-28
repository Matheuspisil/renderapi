from django import forms
from GPC.forms.forms import *
from GPC.models.projetovida import ProjetoVida, Autoconhecimento
from GPC.models.projetovida import PlanejamentoCarreira


class ProjetoVidaForm(forms.ModelForm):
    class Meta:
        model = ProjetoVida
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'area_interesse': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'}),
            'site': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'sobre': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Sobre você'}),
            'competencias': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descreva suas principais competências'}),
            'experiencia': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Detalhe sua experiência profissional'}),
            'formacao_academica': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Nome da Formação'}),
            'instituicao': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Instituição'}),
            'data_inicio': forms.DateInput(attrs={'class': 'form-control', 'required': 'required', 'type': 'date'}),
            'data_termino': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'atual': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descrição'}),
            'licencas_certificados': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Detalhe suas licenças e certificados'}),
            'projetos': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descreva os projetos em que trabalhou'}),
            'trabalho_voluntario': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Detalhe seu trabalho voluntário'}),
            'publicacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Liste suas publicações'}),
            'cursos': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descreva os cursos que realizou'}),
            'idiomas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe os idiomas que você fala'}),
            'interesses': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descreva seus interesses'}),
            'curriculo': forms.FileInput(attrs={'class': 'form-control-file'}),
        }


# class AutoconhecimentoForm(forms.ModelForm):
#     class Meta:
#         model = Autoconhecimento
#         fields = ['etica', 'autoeficacia', 'trabalho_equipe', 'pens_criativo', 'pens_analitico',
#                   'res_problemas', 'comunicacao', 'adaptabilidade', 'persistencia', 'agilidade',
#                   'gestao', 'orient_cliente', 'linguagens', 'programacao', 'ia', 'bigdata', 'ciberseg',
#                   'redes', 'qualidade']
#
#
# class AutoconhecimentoUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Autoconhecimento
#         fields = ['etica', 'autoeficacia', 'trabalho_equipe', 'pens_criativo', 'pens_analitico',
#                   'res_problemas', 'comunicacao', 'adaptabilidade', 'persistencia', 'agilidade',
#                   'gestao', 'orient_cliente', 'linguagens', 'programacao', 'ia', 'bigdata', 'ciberseg',
#                   'redes', 'qualidade']

class AutoconhecimentoForm(forms.ModelForm):
    class Meta:
        model = Autoconhecimento
        fields = [
            'etica', 'autoeficacia', 'trabalho_equipe', 'pens_criativo', 'pens_analitico',
            'res_problemas', 'comunicacao', 'adaptabilidade', 'persistencia', 'agilidade',
            'gestao', 'orient_cliente', 'linguagens', 'programacao', 'ia', 'bigdata',
            'ciberseg', 'redes', 'qualidade'
        ]
        labels = {
            'etica': 'Ética',
            'autoeficacia': 'Autoeficácia',
            'trabalho_equipe': 'Trabalho em Equipe',
            'pens_criativo': 'Pensamento Criativo',
            'pens_analitico': 'Pensamento Analítico',
            'res_problemas': 'Resolução de Problemas',
            'comunicacao': 'Comunicação efetiva',
            'adaptabilidade': 'Adaptabilidade',
            'persistencia': 'Persistência',
            'agilidade': 'Agilidade',
            'gestao': 'Liderança e Gestão',
            'orient_cliente': 'Orientação para o Cliente',
            'linguagens': 'Múltiplas Linguagens',
            'programacao': 'Programação',
            'ia': 'Inteligência Artificial',
            'bigdata': 'Big Data',
            'ciberseg': 'Cibersegurança',
            'redes': 'Redes',
            'qualidade': 'Controle da Qualidade'
        }

        widgets = {
            'etica': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'autoeficacia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'trabalho_equipe': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pens_criativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pens_analitico': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'res_problemas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'comunicacao': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'adaptabilidade': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'persistencia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'agilidade': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'gestao': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'orient_cliente': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'linguagens': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'programacao': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'bigdata': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ciberseg': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'redes': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'qualidade': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
 
class PlanejamentoCarreiraForm(forms.ModelForm):
    curto_prazo_pessoal = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), required=False)
    medio_prazo_pessoal = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), required=False)
    longo_prazo_pessoal = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), required=False)

    curto_prazo_profissional = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), required=False)
    medio_prazo_profissional = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), required=False)
    longo_prazo_profissional = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), required=False)

    metas_especificas = forms.MultipleChoiceField(
        choices=[
            ('Reflexão Profunda', 'Reflexão Profunda'),
            ('Análise do Passado', 'Análise do Passado'),
            ('Busca de Mentoria', 'Busca de Mentoria'),
            ('Desenvolvimento de Novas Habilidades', 'Desenvolvimento de Novas Habilidades'),
            ('Adaptação e Flexibilidade', 'Adaptação e Flexibilidade'),
            ('Busca de Equilíbrio', 'Busca de Equilíbrio'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    planos_acao = forms.MultipleChoiceField(
        choices=[
            ('Organização Doméstica', 'Organização Doméstica'),
            ('Saúde e Bem-estar', 'Saúde e Bem-estar'),
            ('Financeiro Pessoal', 'Financeiro Pessoal'),
            ('Organização do Tempo', 'Organização do Tempo'),
            ('Plano de Carreira', 'Plano de Carreira'),
            ('Plano de Projetos', 'Plano de Projetos'),
            ('Gestão do Tempo', 'Gestão do Tempo'),
            ('Desenvolvimento de Habilidades', 'Desenvolvimento de Habilidades'),
            ('Plano de Networking', 'Plano de Networking'),
            ('Outros', 'Outros'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    outros_texto = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), required=False)
    
    visao_futuro = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)

    estudos = forms.MultipleChoiceField(
        choices=[
            ('Exatas', 'Exatas'),
            ('Biológicas', 'Biológicas'),
            ('Saúde', 'Saúde'),
            ('Engenharia', 'Engenharia'),
            ('Ciências Humanas', 'Ciências Humanas'),
            ('Ciências Sociais Aplicadas', 'Ciências Sociais Aplicadas'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = PlanejamentoCarreira
        fields = [
            'curto_prazo_pessoal',
            'medio_prazo_pessoal',
            'longo_prazo_pessoal',
            'curto_prazo_profissional',
            'medio_prazo_profissional',
            'longo_prazo_profissional',
            'metas_especificas',
            'planos_acao',
            'outros_texto',
            'visao_futuro',
            'estudos'
        ]
