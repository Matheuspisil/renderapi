# Generated by Django 5.0.6 on 2024-08-09 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GPC', '0039_remove_estudo_recomendacao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element_name', models.CharField(max_length=255, unique=True)),
                ('background_color', models.CharField(default='#ffffff', max_length=7)),
                ('text_color', models.CharField(default='#000000', max_length=7)),
            ],
        ),
        migrations.RemoveField(
            model_name='pageconfiguration',
            name='background_color',
        ),
        migrations.RemoveField(
            model_name='pageconfiguration',
            name='text_color',
        ),
        migrations.AddField(
            model_name='pageconfiguration',
            name='element',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GPC.elementconfiguration', verbose_name='Elemento'),
        ),
    ]
