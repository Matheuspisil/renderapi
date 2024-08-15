from .views import *
from .decorators import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from GPC.models.mentor import Mentor, Mentoria
from GPC.models.aluno import Aluno
from GPC.models.vagas import AlunoVaga, Vaga
from GPC.models.projetovida import ProjetoVida, Autoconhecimento

from GPC.forms.formsAluno import AlunoForm, AlunoUpdateForm
from GPC.forms.forms import UsuarioForm


def register_aluno(request):
    if request.method == 'POST':
        user_form = UsuarioForm(request.POST)
        aluno_form = AlunoForm(request.POST)

        if user_form.is_valid() and aluno_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.user_type = 1
            user.username = user.email
            user.save()

            aluno = aluno_form.save(commit=False)
            aluno.user = user
            aluno.save()

            messages.success(
                request, 'Cadastro de aluno realizado com sucesso.')
            return redirect('login')
        else:
            print(user_form.errors)
            print(aluno_form.errors)
    else:
        user_form = UsuarioForm()
        aluno_form = AlunoForm()

    return render(request, 'GPC/aluno/aluno_formulario.html', {'user_form': user_form, 'aluno_form': aluno_form})


@login_required
@user_type_required(user_types=[1])
def aluno_area(request):
    user = request.user
    welcome_message = f"Olá {user.full_name}, Bem-vindo!"
    context = {
        'user': user,
        'welcome_message': welcome_message,
    }
    return render(request, 'GPC/aluno/aluno_area.html', context)


@login_required
@user_type_required(user_types=[1])
def aluno_mentoria(request):
    aluno = Aluno.objects.get(user=request.user)

    # filtrando os mentores do aluno
    mentores_do_aluno = Mentoria.objects.filter(
        aluno_id=aluno.id).values_list('mentor_id', flat=True)

    mentores_nao_relacionados = Mentor.objects.exclude(
        id__in=mentores_do_aluno)

    return render(request, 'GPC/aluno/aluno_mentoria.html', {'aluno': aluno, 'mentores': mentores_nao_relacionados})


@login_required
@user_type_required(user_types=[1])
def aluno_nova_mentoria(request, mentor_id):
    aluno = Aluno.objects.get(user=request.user)
    mentor = get_object_or_404(Mentor, pk=mentor_id)
    area = mentor.area_mentoria
    mentoria = Mentoria.objects.create(aluno=aluno, mentor=mentor, area=area)
    return render(request, 'GPC/aluno/mentoria_solicitada.html', {'mentoria': mentoria})


@login_required
@user_type_required(user_types=[1])
def candidatar_vaga(request, vaga_id):
    aluno = Aluno.objects.get(user=request.user)
    vaga = get_object_or_404(Vaga, id=vaga_id)

    # Verifica se o aluno já se candidatou a essa vaga
    candidatura_existente = AlunoVaga.objects.filter(aluno=aluno, vaga=vaga).exists()
    if candidatura_existente:
        messages.error(request, 'Você já se candidatou a esta vaga.')
        # return redirect('aluno-area', vaga_id=vaga.id) # tratamento aqui "VOCE JA SE CANDIDATOU A ESTA VAGA"
        return redirect('aluno-vagas') # tratamento aqui
  
    AlunoVaga.objects.create(aluno=aluno, vaga=vaga)
    messages.success(request, 'Candidatura realizada com sucesso!')
    # return redirect('vaga_detail', vaga_id=vaga.id) 
    return redirect('aluno-vagas')


@login_required
@user_type_required(user_types=[1])
def aluno_update(request):
    user = request.user
    aluno = Aluno.objects.get(user=user)

    if request.method == 'POST':
        form = AlunoUpdateForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informações atualizadas com sucesso.')
            return redirect('perfil')
        else:
            messages.error(
                request, 'Erro ao atualizar informações. Por favor, corrija os erros abaixo.')
    else:
        form = AlunoUpdateForm(instance=aluno)

    return render(request, 'GPC/aluno/aluno_perfil.html', {'form': form})


# def vagas_recomendadas():
#     score = 0
#     if enfase_aluno == enfase_vaga:
#         score += 50
#     if aluno_interesse == interesse_vaga:
#         score += 20

#     return score

@login_required
@user_type_required(user_types=[1])
def aluno_vagas(request):
    aluno = Aluno.objects.get(user=request.user)
    vagas = Vaga.objects.all()

    # Filtra o ProjetoVida e Autoconhecimento específicos do aluno
    projeto_vida = ProjetoVida.objects.filter(aluno=aluno)
    try:
        autoconhecimento = Autoconhecimento.objects.get(aluno=aluno)
    except Autoconhecimento.DoesNotExist:
        autoconhecimento = Autoconhecimento.objects.create(aluno=aluno)

    def calcular_pontuacao(aluno, vaga):
        '''Calcula a pontuação da vaga com base nos interesses do aluno'''
        score = 0

        vaga_autoconhecimento = {
            'etica': vaga.etica,
            'autoeficacia': vaga.autoeficacia,
            'trabalho_equipe': vaga.trabalho_equipe,
            'pens_criativo': vaga.pens_criativo,
            'pens_analitico': vaga.pens_analitico,
            'res_problemas': vaga.res_problemas,
            'comunicacao': vaga.comunicacao,
            'adaptabilidade': vaga.adaptabilidade,
            'persistencia': vaga.persistencia,
            'agilidade': vaga.agilidade,
            'gestao': vaga.gestao,
            'orient_cliente': vaga.orient_cliente,
            'linguagens': vaga.linguagens,
            'programacao': vaga.programacao,
            'ia': vaga.ia,
            'bigdata': vaga.bigdata,
            'ciberseg': vaga.ciberseg,
            'redes': vaga.redes,
            'qualidade': vaga.qualidade
        }

        aluno_autoconhecimento = {
            'etica': autoconhecimento.etica,
            'autoeficacia': autoconhecimento.autoeficacia,
            'trabalho_equipe': autoconhecimento.trabalho_equipe,
            'pens_criativo': autoconhecimento.pens_criativo,
            'pens_analitico': autoconhecimento.pens_analitico,
            'res_problemas': autoconhecimento.res_problemas,
            'comunicacao': autoconhecimento.comunicacao,
            'adaptabilidade': autoconhecimento.adaptabilidade,
            'persistencia': autoconhecimento.persistencia,
            'agilidade': autoconhecimento.agilidade,
            'gestao': autoconhecimento.gestao,
            'orient_cliente': autoconhecimento.orient_cliente,
            'linguagens': autoconhecimento.linguagens,
            'programacao': autoconhecimento.programacao,
            'ia': autoconhecimento.ia,
            'bigdata': autoconhecimento.bigdata,
            'ciberseg': autoconhecimento.ciberseg,
            'redes': autoconhecimento.redes,
            'qualidade': autoconhecimento.qualidade
        }

        # Adiciona pontuação para cada campo de autoconhecimento desejável coincidente
        for key in vaga_autoconhecimento:
            if vaga_autoconhecimento[key] == aluno_autoconhecimento[key]:
                score += 10

        return score

    # Filtrar e ordenar as vagas com base na pontuação calculada
    vagas_recomendadas = []
    for vaga in vagas:
        pontuacao = calcular_pontuacao(aluno, vaga)
        if pontuacao >= 10:  # Filtro para incluir apenas vagas com pontuação mínima
            vagas_recomendadas.append((vaga, pontuacao))

    # Ordenar as vagas pela pontuação (do maior para o menor)
    vagas_recomendadas = sorted(
        vagas_recomendadas, key=lambda x: x[1], reverse=True)
    vagas = [vaga for vaga, pontuacao in vagas_recomendadas]

    return render(request, 'GPC/aluno/aluno_vagas.html', {'aluno': aluno, 'vagas': vagas})
