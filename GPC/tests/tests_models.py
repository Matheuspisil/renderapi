from django.test import TestCase
from GPC.models import Aluno, Mentor, Empresa, Estagio

class TestModels(TestCase):
    def setUp(self):
        self.aluno_data = {'nome': 'João', 'cpf': '12345678909'}
        self.mentor_data = {'nome': 'Maria', 'cpf': '98765432109'}
        self.empresa_data = {'nome': 'Empresa X', 'cnpj': '12345678901234'}
        self.estagio_data = {'titulo': 'Vaga de Estágio', 'empresa': Empresa.objects.create(**self.empresa_data)}

    def test_aluno_model(self):
        aluno = Aluno.objects.create(**self.aluno_data)
        self.assertEqual(aluno.nome, self.aluno_data['nome'])
        self.assertEqual(aluno.cpf, self.aluno_data['cpf'])

    def test_mentor_model(self):
        mentor = Mentor.objects.create(**self.mentor_data)
        self.assertEqual(mentor.nome, self.mentor_data['nome'])
        self.assertEqual(mentor.cpf, self.mentor_data['cpf'])

    def test_empresa_model(self):
        empresa = Empresa.objects.create(**self.empresa_data)
        self.assertEqual(empresa.nome, self.empresa_data['nome'])
        self.assertEqual(empresa.cnpj, self.empresa_data['cnpj'])

    def test_estagio_model(self):
        estagio = Estagio.objects.create(**self.estagio_data)
        self.assertEqual(estagio.titulo, self.estagio_data['titulo'])
        self.assertEqual(estagio.empresa.nome, self.empresa_data['nome'])
