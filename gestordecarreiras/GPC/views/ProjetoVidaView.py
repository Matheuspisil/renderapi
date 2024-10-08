from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import user_type_required
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.http import HttpResponse
from GPC.forms.formsProjetoVida import ProjetoVidaForm, PlanejamentoCarreiraForm
from GPC.models.aluno import Aluno
from GPC.models.projetovida import *
from ..forms.formsProjetoVida import *
from ..models.projetovida import *
from django.contrib import messages
from django.conf import settings
import requests
import pandas as pd
import os


class ProjetoVidaView(View):
    @method_decorator(login_required)
    @method_decorator(user_type_required(user_types=[1]))
    def get(self, request):
        aluno = Aluno.objects.get(user=request.user)
        projeto_vida = ProjetoVida.objects.filter(aluno=aluno).first()
        
        projeto_vida_form = ProjetoVidaForm(instance=projeto_vida)
        return render(request, 'GPC/aluno/projetodevida/projeto_vida_area.html', {
            'projeto_vida_form': projeto_vida_form, 
            'aluno': aluno
        })


class AutoconhecimentoView(View):
    @method_decorator(login_required)
    @method_decorator(user_type_required(user_types=[1]))
    def get(self, request):
        aluno = Aluno.objects.get(user=request.user)
        autoconhecimento = Autoconhecimento.objects.filter(aluno=aluno).first()
        autoconhecimento_form = AutoconhecimentoForm(instance=autoconhecimento)
        return render(request, 'GPC/aluno/projetodevida/autoconhecimento_formulario.html', {
            'autoconhecimento_form': autoconhecimento_form,
            'aluno': aluno
        })

    @method_decorator(login_required)
    @method_decorator(user_type_required(user_types=[1]))
    def post(self, request):
        aluno = Aluno.objects.get(user=request.user)
        autoconhecimento = Autoconhecimento.objects.filter(aluno=aluno).first()
        if autoconhecimento:
            autoconhecimento_form = AutoconhecimentoForm(request.POST, instance=autoconhecimento)
        else:
            autoconhecimento_form = AutoconhecimentoForm(request.POST)

        if autoconhecimento_form.is_valid():
            autoconhecimento = autoconhecimento_form.save(commit=False)
            autoconhecimento.aluno = aluno
            autoconhecimento.save()
            return redirect('projeto-vida-area')
        else:
            error_message = 'O formulário não pôde ser submetido devido aos seguintes erros:\n'
            for field, errors in autoconhecimento_form.errors.items():
                error_message += f'{field}: {", ".join(errors)}\n'
            return HttpResponse(error_message)


@login_required
@user_type_required(user_types=[1])
def projeto_vida(request):
    aluno = Aluno.objects.get(user=request.user)
    projeto_vida = ProjetoVida.objects.filter(aluno=aluno).first()

    if request.method == 'POST':
        if projeto_vida:
            projeto_vida_form = ProjetoVidaForm(request.POST, request.FILES, instance=projeto_vida)
        else:
            projeto_vida_form = ProjetoVidaForm(request.POST, request.FILES)

        if projeto_vida_form.is_valid():
            projeto_vida = projeto_vida_form.save(commit=False)
            projeto_vida.aluno = aluno  # Associando o aluno ao projeto de vida
            projeto_vida.save()

            pdf = generate_pdf(projeto_vida)
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{projeto_vida.nome} PROJETO_VIDA.pdf"'
            return response
        else:
            error_message = 'O formulário não pôde ser submetido devido aos seguintes erros:\n'
            for field, errors in projeto_vida_form.errors.items():
                error_message += f'{field}: {", ".join(errors)}\n'
            return HttpResponse(error_message)
    else:
        projeto_vida_form = ProjetoVidaForm()

    return render(request, 'GPC/aluno/formulario_projeto_vida.html', {
        'projeto_vida_form': projeto_vida_form, 
        'aluno': aluno
    })

def generate_pdf(projeto_vida):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    width, height = A4

    #cabeçalho
    header_font_size = 18
    body_font_size = 12
    line_height = 20

    p.setFont("Helvetica-Bold", header_font_size)
    nome_width = p.stringWidth(projeto_vida.nome, "Helvetica-Bold", header_font_size)
    nome_x = (width - nome_width) / 2
    p.drawString(nome_x, height - 50, projeto_vida.nome)

    p.setFont("Helvetica", body_font_size)
    endereco_width = p.stringWidth(projeto_vida.endereco, "Helvetica", body_font_size)
    endereco_x = (width - endereco_width) / 2
    p.drawString(endereco_x, height - 80, projeto_vida.endereco)

    telefone_email = f'Telefone: {projeto_vida.telefone} | E-mail: {projeto_vida.email}'
    tel_email_width = p.stringWidth(telefone_email, "Helvetica", body_font_size)
    tel_email_x = (width - tel_email_width) / 2
    p.drawString(tel_email_x, height - 110, telefone_email)

    linkedin_width = p.stringWidth(projeto_vida.linkedin, "Helvetica", body_font_size)
    linkedin_x = (width - linkedin_width)/2
    p.drawString(linkedin_x, height - 140, f'LinkedIn: {projeto_vida.linkedin}')

    p.line(50, height - 160, width - 50, height - 160)

    # Títulos e informações principais
    section_y = height - 180
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, section_y, 'Resumo:')
    p.setFont("Helvetica", body_font_size)
    p.drawString(50, section_y - 20, projeto_vida.sobre)

    section_y -= 60
    p.drawString(50, section_y, 'Competências:')
    p.drawString(50, section_y - 20, projeto_vida.competencias)

    section_y -= 40
    p.drawString(50, section_y, 'Experiência:')
    p.drawString(50, section_y - 20, projeto_vida.experiencia)

    section_y -= 40
    p.drawString(50, section_y, 'Formação Acadêmica:')
    p.drawString(50, section_y - 20, projeto_vida.formacao_academica)

    section_y -= 40
    p.drawString(50, section_y, 'Licenças e Certificados:')
    p.drawString(50, section_y - 20, projeto_vida.licencas_certificados)

    section_y -= 40
    p.drawString(50, section_y, 'Projetos:')
    p.drawString(50, section_y - 20, projeto_vida.projetos)

    section_y -= 40
    p.drawString(50, section_y, 'Trabalho Voluntário:')
    p.drawString(50, section_y - 20, projeto_vida.trabalho_voluntario)

    section_y -= 40
    p.drawString(50, section_y, 'Publicações:')
    p.drawString(50, section_y - 20, projeto_vida.publicacoes)

    section_y -= 40
    p.drawString(50, section_y, 'Idiomas:')
    p.drawString(50, section_y - 20, projeto_vida.idiomas)

    section_y -= 40
    p.drawString(50, section_y, 'Interesses:')
    p.drawString(50, section_y - 20, projeto_vida.interesses)

    section_y -= 40
    p.drawString(50, section_y, 'Instituição:')
    p.drawString(50, section_y - 20, projeto_vida.instituicao)

    section_y -= 40
    p.drawString(50, section_y, 'Data de Início:')
    p.drawString(50, section_y - 20, str(projeto_vida.data_inicio))

    if not projeto_vida.atual:
        section_y -= 40
        p.drawString(50, section_y, 'Data de Término:')
        p.drawString(50, section_y - 20, str(projeto_vida.data_termino))

    section_y -= 40
    p.drawString(50, section_y, 'Descrição:')
    p.drawString(50, section_y - 20, projeto_vida.descricao)

    section_y -= 40
    p.drawString(50, section_y, 'Cursos:')
    p.drawString(50, section_y - 20, projeto_vida.cursos)

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    return pdf

class PlanejamentoCarreiraView(View):
    template_name = 'GPC/aluno/projetodevida/planejamento_form.html'

    def post(self, request, *args, **kwargs):
        form = PlanejamentoCarreiraForm(request.POST)
        if form.is_valid():
            # Capturar os dados de texto (textareas)
            dados_textarea = {
                'curto_prazo_pessoal': form.cleaned_data.get('curto_prazo_pessoal'),
                'medio_prazo_pessoal': form.cleaned_data.get('medio_prazo_pessoal'),
                'longo_prazo_pessoal': form.cleaned_data.get('longo_prazo_pessoal'),
                'curto_prazo_profissional': form.cleaned_data.get('curto_prazo_profissional'),
                'medio_prazo_profissional': form.cleaned_data.get('medio_prazo_profissional'),
                'longo_prazo_profissional': form.cleaned_data.get('longo_prazo_profissional'),
                'outros_texto': form.cleaned_data.get('outros_texto'),
                'visao_futuro': form.cleaned_data.get('visao_futuro'),
            }

            # Capturar os dados booleanos (checkboxes)
            dados_boleanos = {
                'metas_especificas': form.cleaned_data.get('metas_especificas'),
                'planos_acao': form.cleaned_data.get('planos_acao'),
                'estudos': form.cleaned_data.get('estudos'),
            }

            # Enviar os dados para o Langflow em dois grupos separados
            langflow_url = "http://localhost:7860/api/v1/flow"
            
            # Enviar dados de textarea para o Langflow
            response_textarea = requests.post(langflow_url, json=dados_textarea)
            recomendacoes_textarea = response_textarea.json()

            # Enviar dados booleanos para o Langflow
            response_boleanos = requests.post(langflow_url, json=dados_boleanos)
            recomendacoes_boleanos = response_boleanos.json()

            # Processar as recomendações e salvar no modelo
            planejamento_carreira = form.save(commit=False)
            planejamento_carreira.recomendacoes_textarea = recomendacoes_textarea.get('recomendacoes')
            planejamento_carreira.recomendacoes_boleanos = recomendacoes_boleanos.get('recomendacoes')
            planejamento_carreira.save()

            return redirect('resultado_planejamento_carreira', pk=planejamento_carreira.pk)
        
        return render(request, self.template_name, {'form': form})


class ResultadoPlanejamentoView(View):
    template_name = 'GPC/resultado_planejamento_carreira.html'

    def get(self, request, pk, *args, **kwargs):
        planejamento_carreira = PlanejamentoCarreira.objects.get(pk=pk)
        pontuacoes = {
            'GTD': planejamento_carreira.gtd_score,
            'Kanban': planejamento_carreira.kanban_score,
            'Pomodoro': planejamento_carreira.pomodoro_score,
            'Ivy Lee': planejamento_carreira.ivy_lee_score
        }
        melhor_metodologia = max(pontuacoes, key=pontuacoes.get)

        return render(request, self.template_name, {
            'recomendacoes': planejamento_carreira.recomendacoes,
            'pontuacoes': pontuacoes,
            'melhor_metodologia': melhor_metodologia,
            'planejamento_carreira': planejamento_carreira
        })

    
    class ResultadoPlanejamentoCarreiraView(View):
        model = PlanejamentoCarreira
        template_name = 'GPC/aluno/projetodevida/resultado_planejamento_carreira.html'
        context_object_name = 'planejamento_carreira'
