from . views import *
from .decorators import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from GPC.forms.formsMentor import CadastroMentor, MentorUpdateForm
from GPC.forms.forms import UsuarioForm

from GPC.models.mentor import Mentor, Mentoria

from datetime import datetime


def register_mentor(request):
    if request.method == 'POST':
        user_form = UsuarioForm(request.POST)
        mentor_form = CadastroMentor(request.POST)

        if user_form.is_valid() and mentor_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.user_type = 2
            user.username = user.email
            user.save()

            mentor = mentor_form.save(commit=False)
            mentor.user = user
            mentor.save()

            messages.success(
                request, 'Cadastro de mentor realizado com sucesso.')
            return redirect('login')
        else:
            print(user_form.errors)
            print(mentor_form.errors)
    else:
        user_form = UsuarioForm()
        mentor_form = CadastroMentor()

    return render(request, 'GPC/mentor/mentor_cadastro.html', {'user_form': user_form, 'mentor_form': mentor_form})


@login_required
@user_type_required(user_types=[2])
def mentor_area(request):
    mentor = Mentor.objects.all()
    return render(request, 'GPC/mentor/mentor_area.html', {'mentor': mentor})


def listagem_mentor(request):
    lista_mentores = Mentor.objects.all()
    return render(request, 'GPC/mentor/mentor_registros.html', {'lista_mentores': lista_mentores})


@login_required
@user_type_required(user_types=[2])
def mentor_relatorios(request):

    user = request.user
    aluno = None
    mentor = Mentor.objects.get(user=user)
    empresa = None
    mentorias = Mentoria.objects.all().filter(
        mentor__id=mentor.id, data_inicio__isnull=False)

    context = {
        'user': user,
        'aluno': aluno,
        'mentor': mentor,
        'empresa': empresa,
        'mentorias': mentorias,
    }

    pagina = 'GPC/mentor/mentor_relatorios.html'

    return render(request, pagina, context)


@login_required
@user_type_required(user_types=[2])
def mentor_solicitacoes(request):

    user = request.user
    aluno = None
    mentor = Mentor.objects.get(user=user)
    empresa = None
    mentorias = Mentoria.objects.all().filter(
        mentor__id=mentor.id, data_inicio__isnull=True)

    context = {
        'user': user,
        'aluno': aluno,
        'mentor': mentor,
        'empresa': empresa,
        'mentorias': mentorias,
    }

    pagina = 'GPC/mentor/mentor_solicitacoes.html'

    return render(request, pagina, context)


@login_required
@user_type_required(user_types=[2])
def aceitar_mentoria(request, mentoria_id):

    user = request.user
    aluno = None
    mentor = Mentor.objects.get(user=user)
    empresa = None

    mentoria = get_object_or_404(Mentoria, pk=mentoria_id)
    mentoria.ativo = True
    mentoria.data_inicio = datetime.now()
    mentoria.save()

    context = {
        'user': user,
        'aluno': aluno,
        'mentor': mentor,
        'empresa': empresa,
        'mentoria': mentoria,
    }

    pagina = 'GPC/mentor/mentoria_aceita.html'

    return render(request, pagina, context)


@login_required
@user_type_required(user_types=[2])
def mentor_update(request):
    user = request.user
    mentor = Mentor.objects.get(user=user)

    if request.method == 'POST':
        form = MentorUpdateForm(request.POST, instance=mentor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informações atualizadas com sucesso.')
            return redirect('perfil')
        else:
            messages.error(
                request, 'Erro ao atualizar informações. Por favor, corrija os erros abaixo.')
    else:
        form = MentorUpdateForm(instance=mentor)

    return render(request, 'GPC/mentor/mentor_perfil.html', {'form': form})
