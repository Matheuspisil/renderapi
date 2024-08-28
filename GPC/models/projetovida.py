from django.db import models
from GPC.utils.listas import areas_de_interesse
from django.utils import timezone
from GPC.models.aluno import Aluno

def upload_to(instance, filename):
    data_hora_atual = timezone.now().strftime('%Y/%m/%d/%H-%M-%S')
    aluno_email = instance.email if instance.email else 'desconhecido'
    
        # Cria o caminho do arquivo
    return f'GPC/alunos/{aluno_email}/curriculos/{data_hora_atual}/{filename}'

class ProjetoVida(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='projetos_vida', blank=True)
    nome = models.CharField(max_length=255) #nome do documento / projeto / arquivo etc. pode ser o nome do aluno.
    email = models.EmailField()
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    site = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    area_interesse = models.CharField(max_length=50, choices=areas_de_interesse)
    sobre = models.TextField(blank=True, null=True)
    competencias = models.TextField(blank=True, null=True)
    experiencia = models.TextField(blank=True, null=True)
    licencas_certificados = models.TextField(blank=True, null=True)
    projetos = models.TextField(blank=True, null=True)
    trabalho_voluntario = models.TextField(blank=True, null=True)
    publicacoes = models.TextField(blank=True, null=True)
    cursos = models.TextField(blank=True, null=True)
    idiomas = models.TextField(blank=True, null=True)
    interesses = models.TextField(blank=True, null=True)

    formacao_academica = models.TextField(blank=True, null=True)
    instituicao = models.CharField(max_length=255, default='instituicao')
    data_inicio = models.DateField(default=timezone.now)
    data_termino = models.DateField(blank=True, null=True)
    atual = models.BooleanField(default=True)
    descricao = models.TextField(blank=True, null=True)

    curriculo = models.FileField(upload_to=upload_to, blank=True, null=True)

    # from django.core.exceptions import PermissionDenied
    # def get_curriculo_url(self, user):
    # if self.aluno.user == user:
    #     return self.curriculo.url
    # else:
    #     raise PermissionDenied("Você não tem permissão para acessar este arquivo.")

    def __str__(self):
        return self.nome
    

class Curriculo(models.Model):
    pass

class Autoconhecimento(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='autoconhecimento', blank=True)
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

    def __str__(self):
        return self.aluno


class PlanejamentoCarreira(models.Model):
    curto_prazo_pessoal = models.TextField(blank=True, null=True)
    medio_prazo_pessoal = models.TextField(blank=True, null=True)
    longo_prazo_pessoal = models.TextField(blank=True, null=True)

    curto_prazo_profissional = models.TextField(blank=True, null=True)
    medio_prazo_profissional = models.TextField(blank=True, null=True)
    longo_prazo_profissional = models.TextField(blank=True, null=True)

    metas_especificas = models.CharField(max_length=255, blank=True, null=True)
    planos_acao = models.CharField(max_length=255, blank=True, null=True)
    outros_texto = models.TextField(blank=True, null=True)

    visao_futuro = models.TextField(blank=True, null=True)

    estudos = models.CharField(max_length=255, blank=True, null=True)

    recomendacoes = models.TextField(blank=True, null=True)

    melhor_metodologia = models.CharField(max_length=50, blank=True, null=True)

    gtd_score = models.IntegerField(default=0)
    kanban_score = models.IntegerField(default=0)
    pomodoro_score = models.IntegerField(default=0)
    ivy_lee_score = models.IntegerField(default=0)

    def __str__(self):
        return f"Planejamento de Carreira {self.id}"



class MetaEspecifica(models.Model):
    meta = models.CharField(max_length=255)
    GTD = models.IntegerField(default=0)
    Kanban = models.IntegerField(default=0)
    Pomodoro = models.IntegerField(default=0)
    Ivy_Lee = models.IntegerField(default=0)

class PlanoAcao(models.Model):
    plano = models.CharField(max_length=255)
    GTD = models.IntegerField(default=0)
    Kanban = models.IntegerField(default=0)
    Pomodoro = models.IntegerField(default=0)
    Ivy_Lee = models.IntegerField(default=0)

class Estudo(models.Model):
    estudo = models.CharField(max_length=255)
    GTD = models.IntegerField(default=0)
    Kanban = models.IntegerField(default=0)
    Pomodoro = models.IntegerField(default=0)
    Ivy_Lee = models.IntegerField(default=0)

class PlanejamentoParametros(models.Model):
    GTD = models.IntegerField(default=0)
    Kanban = models.IntegerField(default=0)
    Pomodoro = models.IntegerField(default=0)
    Ivy_Lee = models.IntegerField(default=0)