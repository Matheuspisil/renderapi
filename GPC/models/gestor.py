from django.db import models
from GPC.models.models import CustomUser


class Gestor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Gestor'
        verbose_name_plural = 'Gestores'
        ordering = ['user__first_name', 'user__last_name']

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class ElementConfiguration(models.Model):
    element_name = models.CharField(max_length=255, verbose_name='Nome do Elemento', null=True)  # Nome do seletor CSS
    background_color = models.CharField(max_length=15, verbose_name='Cor de Fundo', null=True)
    text_color = models.CharField(max_length=15, verbose_name='Cor do Texto', null=True)

    def __str__(self):
        return f"Configurações do elemento {self.element_name}"


class PageConfiguration(models.Model):
    page_name = models.CharField(max_length=255, unique=True)
    icon = models.ImageField(upload_to='icons/', null=True)
    elements = models.ManyToManyField(ElementConfiguration, verbose_name='Elementos')

    def __str__(self):
        return f"Configurações da página {self.page_name}"