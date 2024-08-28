from django.db import models
from GPC.models.models import CustomUser

class Empresa(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    cnpj = models.CharField(max_length=18, unique=True, verbose_name='CNPJ')
    razao_social = models.CharField(max_length=255, verbose_name='Razão Social')
    telefone = models.CharField(max_length=15, verbose_name='Telefone')
    site = models.URLField(max_length=255, blank=True, null=True, verbose_name='Site')

    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    cep = models.CharField(max_length=9, verbose_name='CEP')
    numero = models.CharField(max_length=10, verbose_name='Número')
    complemento = models.CharField(max_length=255, blank=True, null=True, verbose_name='Complemento')
    bairro = models.CharField(max_length=255, verbose_name='Bairro')
    cidade = models.CharField(max_length=255, verbose_name='Cidade')
    estado = models.CharField(max_length=2, verbose_name='Estado')

    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['user__first_name', 'user__last_name']

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
