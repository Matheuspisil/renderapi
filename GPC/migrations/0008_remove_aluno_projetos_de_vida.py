# Generated by Django 5.0.6 on 2024-06-24 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GPC', '0007_aluno_projetos_de_vida_alter_projetovida_aluno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='projetos_de_vida',
        ),
    ]
