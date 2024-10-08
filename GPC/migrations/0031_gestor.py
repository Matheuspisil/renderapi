# Generated by Django 5.0.6 on 2024-08-02 00:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GPC', '0030_alter_customuser_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gestor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Gestor',
                'verbose_name_plural': 'Gestores',
                'ordering': ['user__first_name', 'user__last_name'],
            },
        ),
    ]
