# Generated by Django 5.0.6 on 2024-06-25 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GPC', '0010_delete_mentoriaa'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Estagio',
            new_name='Vaga',
        ),
        migrations.AlterModelOptions(
            name='vaga',
            options={'ordering': ['data_publicacao'], 'verbose_name': 'Vaga', 'verbose_name_plural': 'Vagas'},
        ),
    ]
