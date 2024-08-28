from django.contrib.auth.decorators import login_required
from .decorators import user_type_required
from django.shortcuts import render, redirect, get_object_or_404
from GPC.models.gestor import PageConfiguration, ElementConfiguration
from GPC.utils.utils import parse_css_and_create_elements, parse_css

from GPC.models.aluno import Aluno
from GPC.models.empresa import Empresa
from GPC.models.mentor import Mentor
from GPC.models.vagas import Vaga

@login_required
@user_type_required(user_types=[4])
def page_configuration_list(request):
    configurations = PageConfiguration.objects.all()
    return render(request, 'GPC/gestor/gestor_area.html', {'configurations': configurations})

@login_required
@user_type_required(user_types=[4])
def reset_configuration_list(request):
    if request.method == 'POST':
        # Apagar todas as entradas associadas
        # 1. Apagar todas as entradas de PageConfiguration
        PageConfiguration.objects.all().delete()

        # 2. Apagar todas as entradas de ElementConfiguration
        ElementConfiguration.objects.all().delete()

        # Processa os arquivos CSS e cria os elementos associados
        parse_css_and_create_elements(r'../gestordecarreiras/GPC/static/GPC/css/index.css', 'Index')
        parse_css_and_create_elements(r'../gestordecarreiras/GPC/static/GPC/css/header.css', 'Header')
        parse_css_and_create_elements(r'../gestordecarreiras/GPC/static/GPC/css/footer.css', 'Footer')

        # Obtém todas as configurações de página
        configurations = PageConfiguration.objects.all()
        return render(request, 'GPC/gestor/gestor_area.html', {'configurations': configurations})

    return redirect('page_configuration_list')

@login_required
@user_type_required(user_types=[4])
def index_configuration_list(request):
    parse_css_and_create_elements(
        r'../gestordecarreiras/GPC/static/GPC/css/index.css',
        'Index'
    )
    configuration = get_object_or_404(PageConfiguration, page_name='Index')
    return render(request, 'GPC/gestor/gestor_area.html', {'configurations': [configuration]})

@login_required
@user_type_required(user_types=[4])
def header_configuration_list(request):
    parse_css_and_create_elements(
        r'../gestordecarreiras/GPC/static/GPC/css/header.css',
        'Header'
    )
    configuration = get_object_or_404(PageConfiguration, page_name='Header')
    return render(request, 'GPC/gestor/gestor_area.html', {'configurations': [configuration]})

@login_required
@user_type_required(user_types=[4])
def footer_configuration_list(request):
    parse_css_and_create_elements(
        r'../gestordecarreiras/GPC/static/GPC/css/footer.css',
        'Footer'
    )
    configuration = get_object_or_404(PageConfiguration, page_name='Footer')
    return render(request, 'GPC/gestor/gestor_area.html', {'configurations': [configuration]})

@login_required
@user_type_required(user_types=[4])
def update_page_configuration(request, config_id):
    config = get_object_or_404(PageConfiguration, id=config_id)

    if request.method == 'POST':
        for element in config.elements.all():
            background_color = request.POST.get(f'{element.id}_background_color')
            text_color = request.POST.get(f'{element.id}_text_color')

            if background_color and text_color:
                element.background_color = background_color
                element.text_color = text_color
                element.save()

        return redirect('page_configuration_list')  # Redireciona para a lista de configurações

    return render(request, 'GPC/gestor/gestor_area.html', {'config': config})

@login_required
@user_type_required(user_types=[4])
def gestor_dashboard(request):
    return render(request, 'GPC/gestor/gestor_dashboard.html')

@login_required
@user_type_required(user_types=[4])
def gestor_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'GPC/gestor/gestor_alunos.html', {'alunos': alunos})

@login_required
@user_type_required(user_types=[4])
def gestor_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'GPC/gestor/gestor_empresas.html', {'empresas': empresas})

@login_required
@user_type_required(user_types=[4])
def gestor_mentores(request):
    mentores = Mentor.objects.all()
    return render(request, 'GPC/gestor/gestor_mentores.html', {'mentores': mentores})

@login_required
@user_type_required(user_types=[4])
def gestor_vagas(request):
    vagas = Vaga.objects.all()
    return render(request, 'GPC/gestor/gestor_vagas.html', {'vagas': vagas})