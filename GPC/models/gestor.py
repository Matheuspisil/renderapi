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


class PageConfiguration(models.Model):
    page_name = models.CharField(max_length=255, unique=True)
    background_color = models.CharField(max_length=7, default="#ffffff")
    text_color = models.CharField(max_length=7, default="#000000")
    icon = models.ImageField(upload_to='icons/', blank=True, null=True)

    def reset_to_default(self):
        self.background_color = "#ffffff"
        self.text_color = "#000000"
        self.icon = None
        self.save()

    def __str__(self):
        return f"{self.page_name} Configuration"