from django.db import models
from GPC.models.empresa import Empresa
from django.utils.text import slugify
from GPC.utils.listas import tipos_vagas

from GPC.models.aluno import Aluno
from GPC.models.projetovida import ProjetoVida

class Vaga(models.Model):
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name='Empresa')

    titulo = models.CharField(max_length=255, verbose_name='Título da Vaga')
    tipo_vaga = models.CharField(
        max_length=100, verbose_name='Tipo da Vaga', choices=tipos_vagas)
    descricao = models.TextField(verbose_name='Descrição da Vaga')
    requisitos = models.TextField(verbose_name='Requisitos')
    data_publicacao = models.DateField(
        verbose_name='Data de Publicação', auto_now_add=True)
    data_encerramento = models.DateField(verbose_name='Data de Encerramento')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    slug = models.SlugField(unique=True, max_length=150)

    # campos de autoconhecimento desejaveis para vaga
    etica = models.BooleanField(default=False)
    autoeficacia = models.BooleanField(default=False)
    trabalho_equipe = models.BooleanField(default=False)
    pens_criativo = models.BooleanField(default=False)
    pens_analitico = models.BooleanField(default=False)
    res_problemas = models.BooleanField(default=False)
    comunicacao = models.BooleanField(default=False)
    adaptabilidade = models.BooleanField(default=False)
    persistencia = models.BooleanField(default=False)
    agilidade = models.BooleanField(default=False)
    gestao = models.BooleanField(default=False)
    orient_cliente = models.BooleanField(default=False)
    linguagens = models.BooleanField(default=False)
    programacao = models.BooleanField(default=False)
    ia = models.BooleanField(default=False)
    bigdata = models.BooleanField(default=False)
    ciberseg = models.BooleanField(default=False)
    redes = models.BooleanField(default=False)
    qualidade = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
        ordering = ['data_publicacao']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class AlunoVaga(models.Model):
    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Aceito', 'Aceito'),
        ('Recusado', 'Recusado'),
    )
    
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='candidaturas')
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE, related_name='candidaturas')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')
    data_solicitacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Solicitação')
    data_decisao = models.DateTimeField(null=True, blank=True, verbose_name='Data da Decisão')

    class Meta:
        verbose_name = 'Candidatura'
        verbose_name_plural = 'Candidaturas'
        unique_together = ('aluno', 'vaga')

    def __str__(self):
        return f'{self.aluno} - {self.vaga} ({self.status})'
