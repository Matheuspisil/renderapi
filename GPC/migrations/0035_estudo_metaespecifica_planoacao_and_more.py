# Generated by Django 5.0.7 on 2024-08-07 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GPC', '0034_remove_aluno_enfase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudo', models.CharField(max_length=255)),
                ('recomendacao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MetaEspecifica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta', models.CharField(max_length=255)),
                ('recomendacao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PlanoAcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plano', models.CharField(max_length=255)),
                ('recomendacao', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='aluno',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='big_data',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='ciencia_dados',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='ciencia_informacao',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='cloud_computing',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='communication',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='competitions',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='competitions_connection',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='computer_vision',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='conferences',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='continuous_learning',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='critical_thinking',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='desafios',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='empresas_cargos',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='events',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='events_connection',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='external_feedback',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='fisica',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='goal_setting',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='internships',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='kpi',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='machine_learning',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='matematica',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='mentor',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='motivacoes_profissionais',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='networking',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='nlp',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='objetivos_carreira',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='online_communities',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='online_communities_connection',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='online_communities_update',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='online_courses',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='open_source',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='open_source_connection',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='portfolio',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='present_work',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='problem_solving',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='project_development',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='publish',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='reflection',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='regular_monitoring',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='scientific_publications',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='self_assessment',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='teamwork',
        ),
        migrations.RemoveField(
            model_name='planejamentocarreira',
            name='volunteer',
        ),
        migrations.AddField(
            model_name='planejamentocarreira',
            name='curto_prazo_pessoal',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planejamentocarreira',
            name='curto_prazo_profissional',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planejamentocarreira',
            name='estudos',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='planejamentocarreira',
            name='longo_prazo_pessoal',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planejamentocarreira',
            name='longo_prazo_profissional',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planejamentocarreira',
            name='medio_prazo_pessoal',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planejamentocarreira',
            name='medio_prazo_profissional',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planejamentocarreira',
            name='metas_especificas',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='planejamentocarreira',
            name='outros_texto',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planejamentocarreira',
            name='planos_acao',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='planejamentocarreira',
            name='recomendacoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planejamentocarreira',
            name='visao_futuro',
            field=models.TextField(blank=True, null=True),
        ),
    ]
