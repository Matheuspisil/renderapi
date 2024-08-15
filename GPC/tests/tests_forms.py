from django.test import TestCase
from GPC.forms import AlunoForm, CadastroMentor, EmpresaForm, EstagioForm
from GPC.models import Empresa

class TestForms(TestCase):
    def setUp(self):
        self.aluno_form_data = {'nome': 'João', 'cpf': '12345678909'}
        self.mentor_form_data = {'nome': 'Maria', 'cpf': '98765432109'}
        self.empresa_form_data = {'nome': 'Empresa X', 'cnpj': '12345678901234'}
        self.empresa = Empresa.objects.create(**self.empresa_form_data)
        self.estagio_form_data = {'titulo': 'Vaga de Estágio', 'empresa': self.empresa.id}

    def test_aluno_form(self):
        form = AlunoForm(self.aluno_form_data)
        self.assertTrue(form.is_valid())

    def test_mentor_form(self):
        form = CadastroMentor(self.mentor_form_data)
        self.assertTrue(form.is_valid())

    def test_empresa_form(self):
        form = EmpresaForm(self.empresa_form_data)
        self.assertTrue(form.is_valid())

    def test_estagio_form(self):
        form = EstagioForm(self.estagio_form_data)
        self.assertTrue(form.is_valid())
