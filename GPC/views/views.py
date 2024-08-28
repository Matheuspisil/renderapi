from django.shortcuts import render
from GPC.models.empresa import Empresa
from GPC.models.aluno import Aluno
from GPC.models.mentor import Mentor
from GPC.forms.forms import CustomLoginForm
from .ProjetoVidaView import projeto_vida
from GPC.models.gestor import ElementConfiguration

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .decorators import *

def index(request):
    elements = ElementConfiguration.objects.all()
    element_configs = {element.element_name: element for element in elements}

    return render(request, 'GPC/pages/index.html', {
        'element_configs': element_configs
    })

def header(request):
    elements = ElementConfiguration.objects.all()
    element_configs = {element.element_name: element for element in elements}

    return render(request, 'GPC/partials/header.html', {
        'element_configs': element_configs
    })

def footer(request):
    elements = ElementConfiguration.objects.all()
    element_configs = {element.element_name: element for element in elements}

    return render(request, 'GPC/partials/footer.html', {
        'element_configs': element_configs
    })

def emconstrucao(request):
    return render(request, 'GPC/pages/emconstrucao.html')

@login_required
@user_type_required(user_types=[1])
def solicitando_mentoria(request):
    return render(request, 'GPC/pages/solicitandomentoria.html')

@login_required
@user_type_required(user_types=[1])
def looping_vaga(request):
    return render(request, 'GPC/pages/looping_vaga.html')

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'GPC/pages/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.user_type == 1:  # aluno
            return reverse_lazy('aluno-area')
        elif user.user_type == 2:  # mentor
            return reverse_lazy('mentor-area')
        elif user.user_type == 3:  # empresa
            return reverse_lazy('empresa_area')
        elif user.user_type == 4:  # gestor
            return reverse_lazy('gestor_dashboard')
        else:
            return reverse_lazy('login')

@login_required
@user_type_required(user_types=[1, 2, 3, 4])
def perfil(request):
    user = request.user
    aluno = None
    mentor = None
    empresa = None

    if user.user_type == 1:
        aluno = Aluno.objects.get(user=user)
        pagina = 'GPC/aluno/aluno_perfil.html'
    elif user.user_type == 2:
        mentor = Mentor.objects.get(user=user)
        pagina = 'GPC/mentor/mentor_perfil.html'
    elif user.user_type == 3:
        empresa = Empresa.objects.get(user=user)
        pagina = 'GPC/empresa/empresa_perfil.html'

    context = {
        'user': user,
        'aluno': aluno,
        'mentor': mentor,
        'empresa': empresa,
    }

    return render(request, pagina, context)

