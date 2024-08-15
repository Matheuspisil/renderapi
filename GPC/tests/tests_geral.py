from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from GPC.models.models import Aluno, ProjetoVida, Mentor, Empresa, Vaga
import pytest

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='testuser@example.com',
            password='password123'
        )
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('password123'))

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email='admin@example.com',
            password='password123'
        )
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)

class AlunoTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            email='aluno@example.com',
            password='password123',
            user_type=1
        )

    def test_create_aluno(self):
        aluno = Aluno.objects.create(
            user=self.user,
            matricula=123456,
            cpf='12345678901',
            data_de_nascimento='2000-01-01',
            sexo='M',
            telefone='1234567890',
            endereco='Rua Exemplo',
            numero=10,
            complemento='Apto 101',
            bairro='Bairro Exemplo',
            cidade='Cidade Exemplo',
            estado='EX',
            cep='12345678',
            curso='Curso Exemplo',
            semestre=1,
            mentoria=False
        )
        self.assertEqual(aluno.user.email, 'aluno@example.com')
        self.assertEqual(aluno.matricula, 123456)
        self.assertEqual(aluno.cpf, '12345678901')

class ProjetoVidaTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            email='aluno@example.com',
            password='password123',
            user_type=1
        )
        self.aluno = Aluno.objects.create(
            user=self.user,
            matricula=123456,
            cpf='12345678901',
            data_de_nascimento='2000-01-01',
            sexo='M',
            telefone='1234567890',
            endereco='Rua Exemplo',
            numero=10,
            complemento='Apto 101',
            bairro='Bairro Exemplo',
            cidade='Cidade Exemplo',
            estado='EX',
            cep='12345678',
            curso='Curso Exemplo',
            semestre=1,
            mentoria=False
        )

    def test_create_projeto_vida(self):
        projeto = ProjetoVida.objects.create(
            aluno=self.aluno,
            nome='Projeto Exemplo',
            area_interesse='Tecnologia',
            endereco='Endereço Exemplo',
            telefone='1234567890',
            email='projeto@example.com',
            site='http://www.projetoexemplo.com'
        )
        self.assertEqual(projeto.nome, 'Projeto Exemplo')
        self.assertEqual(projeto.aluno, self.aluno)

class MentorTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            email='mentor@example.com',
            password='password123',
            user_type=2
        )

    def test_create_mentor(self):
        mentor = Mentor.objects.create(
            user=self.user,
            cpf='12345678901',
            data_de_nascimento='1980-01-01',
            sexo='M',
            telefone='1234567890',
            endereco='Rua Exemplo',
            numero='10',
            complemento='Apto 101',
            bairro='Bairro Exemplo',
            cidade='Cidade Exemplo',
            estado='EX',
            cep='12345678',
            profissao='Profissão Exemplo',
            experiencia_profissional='Experiência Exemplo',
            site='http://www.mentorexemplo.com',
            area_mentoria='Tecnologia'
        )
        self.assertEqual(mentor.user.email, 'mentor@example.com')
        self.assertEqual(mentor.cpf, '12345678901')

class EmpresaTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            email='empresa@example.com',
            password='password123',
            user_type=3
        )

    def test_create_empresa(self):
        empresa = Empresa.objects.create(
            user=self.user,
            cnpj='12345678000190',
            razao_social='Empresa Exemplo',
            endereco='Rua Exemplo',
            numero='10',
            complemento='Apto 101',
            bairro='Bairro Exemplo',
            cidade='Cidade Exemplo',
            estado='EX',
            cep='12345678',
            telefone='1234567890',
            site='http://www.empresaexemplo.com'
        )
        self.assertEqual(empresa.user.email, 'empresa@example.com')
        self.assertEqual(empresa.cnpj, '12345678000190')

class VagaTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            email='empresa@example.com',
            password='password123',
            user_type=3
        )
        self.empresa = Empresa.objects.create(
            user=self.user,
            cnpj='12345678000190',
            razao_social='Empresa Exemplo',
            endereco='Rua Exemplo',
            numero='10',
            complemento='Apto 101',
            bairro='Bairro Exemplo',
            cidade='Cidade Exemplo',
            estado='EX',
            cep='12345678',
            telefone='1234567890',
            site='http://www.empresaexemplo.com'
        )

    def test_create_vaga(self):
        vaga = Vaga.objects.create(
            empresa=self.empresa,
            titulo='Vaga Exemplo',
            descricao='Descrição da Vaga Exemplo',
            requisitos='Requisitos da Vaga Exemplo',
            data_encerramento=timezone.now() + timezone.timedelta(days=30),
            ativo=True
        )
        self.assertEqual(vaga.empresa, self.empresa)
        self.assertEqual(vaga.titulo, 'Vaga Exemplo')

if __name__ == "__main__":
    pytest.main(["--html=reports/test_report.html", "--self-contained-html"])