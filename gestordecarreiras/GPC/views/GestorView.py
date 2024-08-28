from django.shortcuts import render, redirect, get_object_or_404
from GPC.models.gestor import PageConfiguration

from GPC.models.aluno import Aluno
from GPC.models.empresa import Empresa
from GPC.models.mentor import Mentor
from GPC.models.vagas import Vaga

DEFAULT_BACKGROUND_COLOR = '#FFFFFF'
DEFAULT_TEXT_COLOR = '#000000'
DEFAULT_ICON = 'path/to/default/icon.png'

def page_configuration_list(request):
    if request.method == 'POST':
        PageConfiguration.objects.all().update(
            background_color=DEFAULT_BACKGROUND_COLOR,
            text_color=DEFAULT_TEXT_COLOR,
            icon=DEFAULT_ICON
        )
        return redirect('page_configuration_list')

    configurations = PageConfiguration.objects.all()

    return render(request, 'GPC/gestor/gestor_area.html', {'configurations': configurations})

def update_page_configuration(request, config_id):
    config = get_object_or_404(PageConfiguration, id=config_id)

    if request.method == 'POST':
        config.background_color = request.POST.get('background_color', config.background_color)
        config.text_color = request.POST.get('text_color', config.text_color)
        config.save()
        return redirect('page_configuration_list')

    return render(request, 'GPC/gestor/gestor_area.html')


def gestor_dashboard(request):
    return render(request, 'GPC/gestor/gestor_dashboard.html')


def gestor_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'GPC/gestor/gestor_alunos.html', {'alunos': alunos})


def gestor_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'GPC/gestor/gestor_empresas.html', {'empresas': empresas})


def gestor_mentores(request):
    mentores = Mentor.objects.all()
    return render(request, 'GPC/gestor/gestor_mentores.html', {'mentores': mentores})


def gestor_vagas(request):
    vagas = Vaga.objects.all()
    return render(request, 'GPC/gestor/gestor_vagas.html', {'vagas': vagas})