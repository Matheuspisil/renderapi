import os
import django

# Definir o caminho para o módulo de configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestordecarreiras.settings')
django.setup()

from GPC.models import MetaEspecifica, PlanoAcao, Estudo

# Metas Específicas
metas_especificas = [
    {'meta': 'Reflexão Profunda', 'GTD': 4, 'Kanban': 2, 'Pomodoro': 1, 'Ivy_Lee': 3},
    {'meta': 'Análise do Passado', 'GTD': 5, 'Kanban': 3, 'Pomodoro': 2, 'Ivy_Lee': 4},
    {'meta': 'Busca de Mentoria', 'GTD': 3, 'Kanban': 4, 'Pomodoro': 1, 'Ivy_Lee': 1},
    {'meta': 'Desenvolvimento de Novas Habilidades', 'GTD': 2, 'Kanban': 5, 'Pomodoro': 1, 'Ivy_Lee': 1},
    {'meta': 'Adaptação e Flexibilidade', 'GTD': 1, 'Kanban': 4, 'Pomodoro': 5, 'Ivy_Lee': 5},
    {'meta': 'Busca de Equilíbrio', 'GTD': 4, 'Kanban': 3, 'Pomodoro': 2, 'Ivy_Lee': 3},
]

# Planos de Ação
planos_acao = [
    {'plano': 'Organização Doméstica', 'GTD': 4, 'Kanban': 2, 'Pomodoro': 1, 'Ivy_Lee': 3},
    {'plano': 'Saúde e Bem-estar', 'GTD': 5, 'Kanban': 3, 'Pomodoro': 2, 'Ivy_Lee': 4},
    {'plano': 'Financeiro Pessoal', 'GTD': 3, 'Kanban': 4, 'Pomodoro': 1, 'Ivy_Lee': 1},
    {'plano': 'Organização do Tempo', 'GTD': 2, 'Kanban': 5, 'Pomodoro': 1, 'Ivy_Lee': 1},
    {'plano': 'Plano de Carreira', 'GTD': 1, 'Kanban': 4, 'Pomodoro': 5, 'Ivy_Lee': 5},
    {'plano': 'Plano de Projetos', 'GTD': 4, 'Kanban': 3, 'Pomodoro': 2, 'Ivy_Lee': 3},
    {'plano': 'Gestão do Tempo', 'GTD': 4, 'Kanban': 2, 'Pomodoro': 1, 'Ivy_Lee': 3},
    {'plano': 'Desenvolvimento de Habilidades', 'GTD': 5, 'Kanban': 3, 'Pomodoro': 2, 'Ivy_Lee': 4},
    {'plano': 'Plano de Networking', 'GTD': 3, 'Kanban': 4, 'Pomodoro': 1, 'Ivy_Lee': 1},
    {'plano': 'Outros', 'GTD': 3, 'Kanban': 2, 'Pomodoro': 2, 'Ivy_Lee': 3},
]

# Estudos
estudos = [
    {'estudo': 'Exatas', 'GTD': 4, 'Kanban': 2, 'Pomodoro': 1, 'Ivy_Lee': 3},
    {'estudo': 'Biológicas', 'GTD': 5, 'Kanban': 3, 'Pomodoro': 2, 'Ivy_Lee': 4},
    {'estudo': 'Saúde', 'GTD': 3, 'Kanban': 4, 'Pomodoro': 1, 'Ivy_Lee': 1},
    {'estudo': 'Engenharia', 'GTD': 2, 'Kanban': 5, 'Pomodoro': 1, 'Ivy_Lee': 1},
    {'estudo': 'Ciências Humanas', 'GTD': 1, 'Kanban': 4, 'Pomodoro': 5, 'Ivy_Lee': 5},
    {'estudo': 'Ciências Sociais Aplicadas', 'GTD': 4, 'Kanban': 3, 'Pomodoro': 2, 'Ivy_Lee': 3},
]

# Função para criar ou atualizar registros no banco de dados
def create_or_update_model(model, data, unique_field):
    for item in data:
        obj, created = model.objects.update_or_create(
            defaults=item,
            **{unique_field: item[unique_field]}
        )
        if created:
            print(f"{model.__name__} '{item[unique_field]}' criada com sucesso.")
        else:
            print(f"{model.__name__} '{item[unique_field]}' atualizada com sucesso.")

# Carregar dados no banco de dados
create_or_update_model(MetaEspecifica, metas_especificas, 'meta')
create_or_update_model(PlanoAcao, planos_acao, 'plano')
create_or_update_model(Estudo, estudos, 'estudo')
