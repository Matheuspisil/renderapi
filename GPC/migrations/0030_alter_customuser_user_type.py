from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GPC', '0029_alter_vaga_enfase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'aluno'), (2, 'mentor'), (3, 'empresa'), (4, 'gestor')], null=True),
        ),
    ]
