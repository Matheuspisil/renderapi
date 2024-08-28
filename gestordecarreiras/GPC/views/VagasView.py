from django.http import HttpResponseBadRequest
from GPC.forms.formsVagas import VagaForm, UpdateVagaForm
from GPC.models.empresa import Empresa
from GPC.models.vagas import Vaga
from .views import *
from .decorators import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .decorators import user_type_required


@login_required
@user_type_required(user_types=[3])
def create_vaga(request):
    print("View create_vaga chamada")  # Debug statement
    empresa = get_object_or_404(Empresa, user=request.user)
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            vaga = form.save(commit=False)
            vaga.empresa = empresa
            vaga.save()
            messages.success(request, 'Vaga criada com sucesso!')
            return redirect('empresa_vaga_list', pk=empresa.pk)
        else:
            print("Formulário inválido")  # Debug statement
            print(form.errors)  # Debug statement
            return HttpResponseBadRequest('Formulário inválido. Verifique os campos.')
    else:
        form = VagaForm()
    return render(request, 'GPC/vaga/vaga_form.html', {'form': form, 'empresa': empresa})


@login_required
@user_type_required(user_types=[3])
def vagas_list(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    vagas = Vaga.objects.filter(empresa=empresa)
    return render(request, 'GPC/vaga/vaga_list.html', {'vagas': vagas, 'empresa': empresa})


@login_required
@user_type_required(user_types=[3])
def vagas_list_slug(request, pk, slug):
    empresa = get_object_or_404(Empresa, pk=pk)
    vagas = Vaga.objects.filter(empresa=empresa, slug=slug)
    return render(request, 'GPC/vaga/vaga_list.html', {'vagas': vagas})


@login_required
@user_type_required(user_types=[3])
def vaga_detail(request, slug):
    user = request.user
    empresa = get_object_or_404(Empresa, user=user)
    vaga = get_object_or_404(Vaga, slug=slug, empresa=empresa)
    return render(request, 'GPC/vaga/vaga_detail.html', {'vaga': vaga, 'empresa': empresa})


@login_required
@user_type_required(user_types=[3])
def update_vaga(request, slug):
    empresa = Empresa.objects.get(user=request.user)
    vaga = get_object_or_404(Vaga, slug=slug, empresa=empresa)
    if request.method == 'POST':
        form = UpdateVagaForm(request.POST, instance=vaga)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vaga atualizada com sucesso!')
            return redirect('vaga_detail', slug=vaga.slug)
        else:
            print(form.errors)
            return HttpResponseBadRequest('Formulário inválido. Verifique os campos.')
    else:
        form = UpdateVagaForm(instance=vaga)
    return render(request, 'GPC/vaga/vaga_form.html', {'form': form})


@login_required
@user_type_required(user_types=[3])
def delete_vaga(request, slug):
    empresa = get_object_or_404(Empresa, user=request.user)
    vaga = get_object_or_404(Vaga, slug=slug, empresa=empresa)
    if request.method == 'POST':
        vaga.delete()
        messages.success(request, 'Vaga deletada com sucesso!')
        return redirect('empresa_vaga_list', pk=empresa.pk)
    return render(request, 'GPC/vaga/vaga_delete.html', {'vaga': vaga, 'empresa': empresa})


def my_view(request):
    context = {
        'version': settings.STATIC_VERSION,
    }
    return render(request, 'base.html', context)

# Aluno


@login_required
@user_type_required(user_types=[1])
def aluno_detalhes_vaga(request, slug):
    vaga = get_object_or_404(Vaga, slug=slug)
    return render(request, 'GPC/aluno/aluno_detalhes_vaga.html', {'vaga': vaga})
