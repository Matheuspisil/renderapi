# Generated by Django 5.0.6 on 2024-06-20 01:10

import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=18, unique=True, verbose_name='CNPJ')),
                ('razao_social', models.CharField(max_length=255, verbose_name='Razão Social')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=255, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=255, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=255, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('site', models.URLField(blank=True, max_length=255, null=True, verbose_name='Site')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'ordering': ['user__first_name', 'user__last_name'],
            },
        ),
        migrations.CreateModel(
            name='ProjetoVida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('area_interesse', models.CharField(choices=[('analise_numerica', 'Análise Numérica'), ('estatistica', 'Estatística'), ('pesquisa_operacional', 'Pesquisa Operacional'), ('big_data', 'Big Data'), ('machine_learning', 'Machine Learning'), ('visualizacao_dados', 'Visualização de Dados'), ('algoritmos', 'Algoritmos e Estruturas de Dados'), ('seguranca_informacao', 'Segurança da Informação'), ('desenvolvimento_software', 'Desenvolvimento de Software'), ('fisica_computacional', 'Física Computacional'), ('modelagem_simulacao', 'Modelagem e Simulação'), ('inteligencia_artificial', 'Inteligência Artificial Aplicada')], max_length=50)),
                ('endereco', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('site', models.URLField(blank=True, null=True)),
                ('sobre', models.TextField(blank=True, null=True)),
                ('competencias', models.TextField(blank=True, null=True)),
                ('experiencia', models.TextField(blank=True, null=True)),
                ('formacao_academica', models.TextField(blank=True, null=True)),
                ('licencas_certificados', models.TextField(blank=True, null=True)),
                ('projetos', models.TextField(blank=True, null=True)),
                ('trabalho_voluntario', models.TextField(blank=True, null=True)),
                ('publicacoes', models.TextField(blank=True, null=True)),
                ('cursos', models.TextField(blank=True, null=True)),
                ('idiomas', models.TextField(blank=True, null=True)),
                ('interesses', models.TextField(blank=True, null=True)),
                ('curriculo', models.FileField(blank=True, null=True, upload_to='curriculos/')),
                ('instituicao', models.CharField(default='instituicao', max_length=255)),
                ('data_inicio', models.DateField(default=django.utils.timezone.now)),
                ('data_termino', models.DateField(blank=True, null=True)),
                ('atual', models.BooleanField(default=True)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estagio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título da Vaga')),
                ('descricao', models.TextField(verbose_name='Descrição da Vaga')),
                ('requisitos', models.TextField(verbose_name='Requisitos')),
                ('data_publicacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Publicação')),
                ('data_encerramento', models.DateTimeField(verbose_name='Data de Encerramento')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPC.empresa', verbose_name='Empresa')),
            ],
            options={
                'verbose_name': 'Estagio',
                'verbose_name_plural': 'Estagios',
                'ordering': ['data_publicacao'],
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'aluno'), (2, 'mentor'), (3, 'empresa')], null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('data_de_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(max_length=255, verbose_name='Sexo')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=255, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=255, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=255, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('profissao', models.CharField(max_length=100, verbose_name='Profissão')),
                ('experiencia_profissional', models.CharField(max_length=255, verbose_name='Experiência')),
                ('disponibilidade_mentoria', models.CharField(max_length=255, verbose_name='Disponibilidade')),
                ('site', models.URLField(blank=True, max_length=255, null=True, verbose_name='Site')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Mentor',
                'verbose_name_plural': 'Mentores',
                'ordering': ['user__first_name', 'user__last_name'],
            },
        ),
        migrations.AddField(
            model_name='empresa',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.PositiveIntegerField(unique=True, verbose_name='Matrícula')),
                ('cpf', models.PositiveIntegerField(unique=True, verbose_name='CPF')),
                ('data_de_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=10, verbose_name='Sexo')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('numero', models.PositiveIntegerField(verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=255, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=255, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=255, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('curso', models.CharField(choices=[('MTI', 'Bacharelado em Matemática da Tecnologia e Inovação'), ('IMPA-MAT-MS', 'Mestrado em Matemática (M.Sc.)'), ('IMPA-MAP-MS', 'Mestrado em Matemática Aplicada (M.Sc.)'), ('IMPA-MAT-PHD', 'Doutorado em Matemática (Ph.D.)'), ('IMPA-MAP-PHD', 'Doutorado em Matemática Aplicada (Ph.D.)'), ('IMPA-ESC-VER', 'Escola de Verão'), ('IMPA-ESC-MAT-AP', 'Escola de Matemática Aplicada'), ('IMPA-PJT-VER', 'Programas de Verão para Jovens Talentos'), ('IMPA-PAPMEM', 'Programa de Aperfeiçoamento de Professores de Matemática (PAPMEM)'), ('IMPA-IC', 'Programa de Iniciação Científica'), ('IMPA-PIC', 'Programa de Iniciação Científica para Jovens (PIC)'), ('IMPA-MINI', 'Minicursos Avançados em Matemática'), ('IMPA-WORK', 'Workshops em Diversas Áreas da Matemática'), ('IMPA-CONF', 'Conferências Temáticas'), ('IMPA-POS-DOC', 'Curso de Pós-Doutorado'), ('IMPA-EST-PESQ', 'Estágios de Pesquisa'), ('IMPA-DIVUL', 'Cursos de Divulgação Científica'), ('IMPA-OFP', 'Oficinas para Professores do Ensino Básico'), ('IMPA-EDU-CONT', 'Programas de Educação Continuada'), ('IMPA-COLAB', 'Programas de Colaboração com Outras Instituições'), ('IMPA-INT-EXCH', 'Programas de Intercâmbio Internacional'), ('IMPA-ONLINE', 'Cursos Online de Matemática e Matemática Aplicada'), ('IMPA-DIST', 'Cursos à Distância para Professores e Estudantes')], max_length=100, verbose_name='Curso')),
                ('semestre', models.IntegerField(verbose_name='Semestre')),
                ('mentoria', models.BooleanField(default=False, verbose_name='Mentoria')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
                'ordering': ['user__first_name', 'user__last_name'],
            },
        ),
    ]
