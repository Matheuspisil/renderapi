# Generated by Django 5.0.6 on 2024-08-14 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GPC', '0040_elementconfiguration_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pageconfiguration',
            name='element',
        ),
        migrations.AddField(
            model_name='pageconfiguration',
            name='elements',
            field=models.ManyToManyField(blank=True, to='GPC.elementconfiguration', verbose_name='Elementos'),
        ),
    ]
