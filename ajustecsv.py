import csv
import os
from django.core.management.base import BaseCommand
from GPC.models.projetovida import MetaEspecifica, PlanoAcao, Estudo

class Command(BaseCommand):
    help = 'Load CSV data into the database'

    def handle(self, *args, **kwargs):
        self.load_metas_especificas()
        self.load_planos_acao()
        self.load_estudos()

    def load_metas_especificas(self):
        file_path = os.path.join('media', 'GPC', 'arquivos', 'metasespecificas.csv')
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            MetaEspecifica.objects.all().delete()  # Clear existing data
            for row in reader:
                MetaEspecifica.objects.create(
                    meta=row['meta'],
                    GTD=int(row['GTD']),
                    Kanban=int(row['Kanban']),
                    Pomodoro=int(row['Pomodoro']),
                    Ivy_Lee=int(row['Ivy Lee'])
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded metas_especificas.csv'))

    def load_planos_acao(self):
        file_path = os.path.join('media', 'GPC', 'arquivos', 'planosdeacao.csv')
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            PlanoAcao.objects.all().delete()  # Clear existing data
            for row in reader:
                PlanoAcao.objects.create(
                    plano=row['plano'],
                    GTD=int(row['GTD']),
                    Kanban=int(row['Kanban']),
                    Pomodoro=int(row['Pomodoro']),
                    Ivy_Lee=int(row['Ivy Lee'])
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded planosdeacao.csv'))

    def load_estudos(self):
        file_path = os.path.join('media', 'GPC', 'arquivos', 'meusestudos.csv')
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            Estudo.objects.all().delete()  # Clear existing data
            for row in reader:
                Estudo.objects.create(
                    estudo=row['estudo'],
                    GTD=int(row['GTD']),
                    Kanban=int(row['Kanban']),
                    Pomodoro=int(row['Pomodoro']),
                    Ivy_Lee=int(row['Ivy Lee'])
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded meusestudos.csv'))
