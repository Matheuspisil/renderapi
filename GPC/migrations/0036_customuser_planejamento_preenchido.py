# Generated by Django 5.0.7 on 2024-08-08 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GPC', '0035_estudo_metaespecifica_planoacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='planejamento_preenchido',
            field=models.BooleanField(default=False),
        ),
    ]
