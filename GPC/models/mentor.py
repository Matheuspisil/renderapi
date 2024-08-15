from django.db import models
from GPC.utils.listas import areas_mentoria
from GPC.models.models import CustomUser
from GPC.models.aluno import Aluno


class Mentor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    data_de_nascimento = models.DateField(verbose_name='Data de Nascimento')
    sexo = models.CharField(max_length=255, verbose_name='Sexo')
    telefone = models.CharField(max_length=15, verbose_name='Telefone')

    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    numero = models.CharField(max_length=10, verbose_name='Número')
    complemento = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Complemento')
    bairro = models.CharField(max_length=255, verbose_name='Bairro')
    cidade = models.CharField(max_length=255, verbose_name='Cidade')
    estado = models.CharField(max_length=2, verbose_name='Estado')
    cep = models.CharField(max_length=9, verbose_name='CEP')

    profissao = models.CharField(max_length=100, verbose_name='Profissão')
    experiencia_profissional = models.CharField(
        max_length=255, verbose_name='Experiência')
    site = models.URLField(max_length=255, blank=True,
                           null=True, verbose_name='Site')
    area_mentoria = models.CharField(
        max_length=100, verbose_name='Mentoria', choices=areas_mentoria)

    class Meta:
        verbose_name = 'Mentor'
        verbose_name_plural = 'Mentores'
        ordering = ['user__first_name', 'user__last_name']

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Mentoria(models.Model):
    aluno = models.ForeignKey(
        Aluno, on_delete=models.CASCADE, verbose_name="Aluno")
    mentor = models.ForeignKey(
        Mentor, on_delete=models.CASCADE, verbose_name="Mentor")

    area = models.TextField(verbose_name="Área da Mentoria")
    ativo = models.BooleanField(default=False, verbose_name="Ativo")
    data_solicitacao = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de solicitação")
    data_inicio = models.DateTimeField(
        blank=True, null=True, verbose_name="Data de início")
    data_fim = models.DateTimeField(
        verbose_name="Data de fim", blank=True, null=True)

    class Meta:
        verbose_name = 'Mentoria'
        verbose_name_plural = 'Mentorias'
        ordering = ['data_inicio']

    def __str__(self):
        return f"Mentoria em {self.area}"
