from django.urls import path
from django.contrib.auth import views as auth_views
from GPC.views import views
from GPC.views.views import CustomLoginView
from GPC.views.decorators import unauthenticated_user
from GPC.views.ProjetoVidaView import ProjetoVidaView, AutoconhecimentoView, PlanejamentoCarreiraView, ResultadoPlanejamentoView, generate_pdf
from GPC.views import AlunoView, EmpresaView, MentorView, VagasView, GestorView
from GPC.views.GestorView import page_configuration_list, reset_configuration_list, update_page_configuration, index_configuration_list, header_configuration_list, footer_configuration_list, gestor_dashboard, gestor_alunos, gestor_empresas, gestor_mentores, gestor_vagas

from GPC.views.EmpresaView import atualizar_solicitacao

urlpatterns = [
    path('', views.index, name='index'),
    
    path('login/', unauthenticated_user(CustomLoginView.as_view()), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('emconstrucao/', views.emconstrucao, name='em_construcao'),
    path('solicitando-mentoria/', views.solicitando_mentoria, name='solicitando_mentoria'),
    path('candidatando-se/', views.looping_vaga, name='looping-vaga'),
    path('perfil/', views.perfil, name='perfil'),

    # ProjetoVida
    path('projetovida/', views.projeto_vida, name='projeto-vida'),
    path('projeto-vida-area/', ProjetoVidaView.as_view(), name='projeto-vida-area'),
    path('autoconhecimento/', AutoconhecimentoView.as_view(), name='autoconhecimento-formulario'),
    path('planejamento/carreira/', PlanejamentoCarreiraView.as_view(), name='planejamento_carreira'),
    path('resultado_planejamento_carreira/<int:pk>/', ResultadoPlanejamentoView.as_view(), name='resultado_planejamento_carreira'),

    # Aluno
    path('aluno/cadastro', AlunoView.register_aluno, name='formulario-aluno'),
    path('aluno/area/', AlunoView.aluno_area, name='aluno-area'),
    path('aluno/update/', AlunoView.aluno_update, name='aluno-update'),
    path('aluno/vagas/', AlunoView.aluno_vagas, name='aluno-vagas'),
    path('aluno/vaga/detalhes/<slug:slug>/', VagasView.aluno_detalhes_vaga, name='aluno-detalhes-vaga'),
    path('aluno/mentoria/', AlunoView.aluno_mentoria, name='aluno-mentoria'),
    path('aluno/mentoria/<int:mentor_id>', AlunoView.aluno_nova_mentoria, name='aluno_nova_mentoria'),
    path('aluno/vaga/<int:vaga_id>', AlunoView.candidatar_vaga, name='aluno-candidatar-se'),
    path('aluno/candidaturas/', AlunoView.aluno_candidaturas, name='aluno-candidaturas'),
    path('download-curriculo/<int:id>', generate_pdf, name='download_curriculo'),

    # Mentor
    path('mentor/cadastro', MentorView.register_mentor, name='mentor_cadastro'),
    path('mentor/area/', MentorView.mentor_area, name="mentor-area"),
    path('mentor/update', MentorView.mentor_update, name="mentor-update"),
    path('mentor/registros', MentorView.listagem_mentor, name='mentor_registros'),
    path('mentor/relatorios', MentorView.mentor_relatorios, name="mentor_relatorios"),
    path('mentor/solicitacoes', MentorView.mentor_solicitacoes, name="mentor_solicitacoes"),
    path('mentor/solicitacoes/<int:mentoria_id>', MentorView.aceitar_mentoria, name='aceitar_mentoria'),
    
    # Empresa
    path('empresa/cadastro/', EmpresaView.register_empresa, name='create_empresa'),

    path('empresa/vagas/', VagasView.vagas_list, name='empresa_vaga_list'),

    path('empresa/solicitacoes/', EmpresaView.solicitacoes_alunos, name='solicitacoes-alunos'),
    path('solicitacao/<str:acao>/<int:solicitacao_id>/', atualizar_solicitacao, name='atualizar_solicitacao'),
    
    path('empresa/area/', EmpresaView.empresa_area, name='empresa_area'),
    path('empresa/<int:pk>/vaga/', VagasView.vagas_list, name='empresa_vaga_list'),
    path('empresa/<int:pk>/vaga/vagas_list/<slug:slug>/', VagasView.vagas_list_slug, name='empresa_vaga_list_slug'),
    path('empresa/update/', EmpresaView.update_empresa, name='empresa_update'),
    path('empresa/', EmpresaView.empresa_list, name='empresa_list'),
    path('empresa/<int:pk>/delete/', EmpresaView.delete_empresa, name='delete_empresa'),
    path('empresa/dashboard/<int:pk>/', EmpresaView.empresa_dashboard, name='empresa_dashboard'),
    path('empresa/talentos/', EmpresaView.empresa_hunter, name='empresa_hunter'),
    
    # Vagas
    path('vagas/', VagasView.vagas_list, name='vaga_list'),
    path('vaga/create/', VagasView.create_vaga, name='create_vaga'),
    path('vaga/<slug:slug>/', VagasView.vaga_detail, name='vaga_detail'),
    path('vaga/<slug:slug>/edit/', VagasView.update_vaga, name='update_vaga'),
    path('vaga/<slug:slug>/delete/', VagasView.delete_vaga, name='delete_vaga'),

    # Gestor
    path('page-configurations/', page_configuration_list, name='page_configuration_list'),
    path('page-configurations/reset/', reset_configuration_list, name='reset_configuration_list'),
    path('page-configurations/update/<int:config_id>/', update_page_configuration, name='update_page_configuration'),
    path('configuracao/index/', index_configuration_list, name='index_configuration_list'),
    path('configuracao/header/', header_configuration_list, name='header_configuration_list'),
    path('configuracao/footer/', footer_configuration_list, name='footer_configuration_list'),
    path('gestor/dashboard/', GestorView.gestor_dashboard, name='gestor_dashboard'),
    path('gestor/alunos/', GestorView.gestor_alunos, name='gestor_alunos'),
    path('gestor/empresas/', GestorView.gestor_empresas, name='gestor_empresas'),
    path('gestor/mentores/', GestorView.gestor_mentores, name='gestor_mentores'),
    path('gestor/vagas/', GestorView.gestor_vagas, name='gestor_vagas'),
]
