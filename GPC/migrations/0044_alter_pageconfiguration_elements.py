# Generated by Django 5.0.6 on 2024-08-16 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GPC', '0043_alter_elementconfiguration_background_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageconfiguration',
            name='elements',
            field=models.ManyToManyField(to='GPC.elementconfiguration', verbose_name='Elementos'),
        ),
    ]
