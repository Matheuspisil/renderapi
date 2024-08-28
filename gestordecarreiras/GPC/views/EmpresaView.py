from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .decorators import user_type_required
from GPC.forms.formsEmpresa import EmpresaForm, EmpresaUpdateForm
from GPC.forms.forms import UsuarioForm
from GPC.models.empresa import Empresa
from GPC.models.vagas import AlunoVaga, Vaga
from GPC.models.aluno import Aluno
from GPC.models.projetovida import Autoconhecimento


def register_empresa(request):
    if request.method == 'POST':
        user_form = UsuarioForm(request.POST)
        empresa_form = EmpresaForm(request.POST)
        if user_form.is_valid() and empresa_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.user_type = 3
            user.username = user.email
            user.save()

            empresa = empresa_form.save(commit=False)
            empresa.user = user
            empresa.save()

            messages.success(request, 'Cadastro de empresa realizado com sucesso.')
            return redirect('login')
        else:
            print(user_form.errors)
            print(empresa_form.errors)
    else:
        user_form = UsuarioForm()
        empresa_form = EmpresaForm()

    return render(request, 'GPC/empresa/empresa_form.html', {'user_form': user_form, 'empresa_form': empresa_form})

@login_required
@user_type_required(user_types=[3])
def empresa_area(request):
    empresa = Empresa.objects.get(user=request.user)
    return render(request, 'GPC/empresa/empresa_area.html', {'empresa': empresa})

@login_required
@user_type_required(user_types=[3])
def update_empresa(request):
    user = request.user
    empresa = Empresa.objects.get(user=user)
    if request.method == "POST":
        empresa_form = EmpresaUpdateForm(request.POST, instance=empresa)
        if empresa_form.is_valid():
            empresa_form.save()
            messages.success(request, 'Empresa atualizada com sucesso!')
            return redirect('perfil')
        else:
            messages.error(request, 'Erro ao atualizar informações. Por favor, corrija os erros abaixo.')
    else:
        empresa_form = EmpresaUpdateForm(instance=empresa)
    return render(request, 'GPC/empresa/empresa_perfil.html', {'empresa_form': empresa_form})

def empresa_list(request):
    empresas = Empresa.objects.all()
    return render(request, 'GPC/empresa/empresa_list.html', {'empresas': empresas})

@login_required
@user_type_required(user_types=[3])
def delete_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == "POST":
        empresa.delete()
        messages.success(request, 'Empresa excluída com sucesso!')
        return redirect('empresa_list')
    return render(request, 'GPC/empresa/empresa_confirm_delete.html', {'empresa': empresa})

@login_required
@user_type_required(user_types=[3])
def empresa_dashboard(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    return render(request, 'GPC/empresa/empresa_dashboard.html', {'empresa': empresa})

@login_required
def perfil(request):
    user = request.user
    empresa = Empresa.objects.get(user=user)
    if request.method == "POST":
        user_form = UsuarioForm(request.POST, instance=user)
        empresa_form = EmpresaForm(request.POST, instance=empresa)
        if user_form.is_valid() and empresa_form.is_valid():
            user_form.save()
            empresa_form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('perfil')
        else:
            messages.error(request, 'Erro ao atualizar perfil. Verifique os campos.')
    else:
        user_form = UsuarioForm(instance=user)
        empresa_form = EmpresaForm(instance=empresa)
    return render(request, 'GPC/empresa/empresa_perfil.html', {'user_form': user_form, 'empresa_form': empresa_form, 'empresa': empresa})

@login_required
def empresa_hunter(request):
    '''Retorna uma lista de alunos em ordem de pontuação (baseado nos checkboxes do template)'''
    filters = [
        'etica', 'autoeficacia', 'trabalho_equipe', 'pens_criativo', 'pens_analitico', 'res_problemas',
        'comunicacao', 'adaptabilidade', 'persistencia', 'agilidade', 'gestao', 'orient_cliente', 
        'linguagens', 'programacao', 'ia', 'bigdata', 'ciberseg', 'redes', 'qualidade'
    ]

    alunos = Aluno.objects.all()

    alunos_pontuados = []
    for aluno in alunos:
        try:
            autoconhecimento = Autoconhecimento.objects.get(aluno=aluno)
        except Autoconhecimento.DoesNotExist:
            continue

        pontuacao = 0
        for filtro in filters:
            # Verifica se o filtro está presente na query string e se o atributo correspondente é True
            if request.GET.get(filtro) == 'True' and getattr(autoconhecimento, filtro, False):
                pontuacao += 1
        
        alunos_pontuados.append((aluno, pontuacao))

    # Ordenar os alunos pela pontuação (do maior para o menor)
    alunos_pontuados = sorted(alunos_pontuados, key=lambda x: x[1], reverse=True)
    alunos = [aluno for aluno, pontuacao in alunos_pontuados]

    return render(request, 'GPC/empresa/empresa_hunter.html', {'alunos': alunos})


@login_required
@user_type_required(user_types=[3])
def solicitacoes_alunos(request):
    empresa = get_object_or_404(Empresa, user=request.user)
    solicitacoes = AlunoVaga.objects.filter(vaga__empresa=empresa, status='Pendente')
    
    return render(request, 'GPC/empresa/listar_solicitacoes.html', {'solicitacoes': solicitacoes})

@login_required
@user_type_required(user_types=[3])
def atualizar_solicitacao(request, solicitacao_id, acao):
    solicitacao = get_object_or_404(AlunoVaga, id=solicitacao_id)
    
    if acao == 'aceitar':
        solicitacao.status = 'Aceito'
    elif acao == 'recusar':
        solicitacao.status = 'Recusado'
    
    solicitacao.data_decisao = timezone.now()
    solicitacao.save()
    
    return redirect('solicitacoes-alunos')