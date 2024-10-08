# Generated by Django 5.0.7 on 2024-08-08 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GPC', '0038_rename_gtd_planejamentocarreira_gtd_score_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudo',
            name='recomendacao',
        ),
        migrations.RemoveField(
            model_name='metaespecifica',
            name='recomendacao',
        ),
        migrations.RemoveField(
            model_name='planoacao',
            name='recomendacao',
        ),
        migrations.AddField(
            model_name='estudo',
            name='GTD',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='estudo',
            name='Ivy_Lee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='estudo',
            name='Kanban',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='estudo',
            name='Pomodoro',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='metaespecifica',
            name='GTD',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='metaespecifica',
            name='Ivy_Lee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='metaespecifica',
            name='Kanban',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='metaespecifica',
            name='Pomodoro',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='planoacao',
            name='GTD',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='planoacao',
            name='Ivy_Lee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='planoacao',
            name='Kanban',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='planoacao',
            name='Pomodoro',
            field=models.IntegerField(default=0),
        ),
    ]
