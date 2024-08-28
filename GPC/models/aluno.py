from datetime import date
from django.db import models
from GPC.utils.listas import cursos_impa
from GPC.models.models import CustomUser


class Aluno(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    # ainda nao sabemos o tamanho da matricula
    matricula = models.PositiveIntegerField(
        unique=True, verbose_name='Matrícula')
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    data_de_nascimento = models.DateField(verbose_name='Data de Nascimento')
    sexo = models.CharField(max_length=10, verbose_name='Sexo', choices=[
                            ('M', 'Masculino'), ('F', 'Feminino')])
    telefone = models.CharField(max_length=15, verbose_name='Telefone')

    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    numero = models.PositiveIntegerField(verbose_name='Número')
    complemento = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Complemento')
    bairro = models.CharField(max_length=255, verbose_name='Bairro')
    cidade = models.CharField(max_length=255, verbose_name='Cidade')
    estado = models.CharField(max_length=2, verbose_name='Estado')
    cep = models.CharField(max_length=9, verbose_name='CEP')

    curso = models.CharField(max_length=100, verbose_name='Curso', choices=cursos_impa)
    semestre = models.IntegerField(verbose_name='Semestre')

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['user__first_name', 'user__last_name']

    @property
    def localidade(self):
        return f'{self.endereco}, {self.numero}, {self.bairro}, {self.cidade} - {self.estado} - {self.cep}'

    @property
    def idade(self):
        if self.data_de_nascimento:
            today = date.today()
            return today.year - self.data_de_nascimento.year - ((today.month, today.day) < (self.data_de_nascimento.month, self.data_de_nascimento.day))
        return None

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


