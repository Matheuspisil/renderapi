# Gestor de carreiras

## Visão do Produto

---

### Sumário

1. [Introdução](#introducao)
2. [Análise de Contexto](#analise-de-contexto)
   1. [Detalhamento da Necessidade](#detalhamento-da-necessidade)
      - [Descrição do Problema](#descricao-do-problema)
      - [Partes Afetadas](#partes-afetadas)
      - [Impacto](#impacto)
      - [Solução de Sucesso](#solucao-de-sucesso)
3. [Partes Interessadas](#partes-interessadas)
   1. [Partes Interessadas](#lista-de-partes-interessadas)
   2. [Usuários](#usuarios)
   3. [Necessidades das Partes Interessadas ou Usuários](#necessidades-das-partes-interessadas-ou-usuarios)
      - [<Empresas>](#Empresas)
      - [<Estudantes>](#Estudantes)
      - [<Mentores>](#Mentores)
4. [Objetivos de Negócio](#objetivos-de-negocio)
5. [Visão Geral do Produto](#visao-geral-do-produto)
   1. [Perspectiva do Produto](#perspectiva-do-produto)
   2. [Características-Chave do Produto](#caracteristicas-chave-do-produto)
      - [Requisitos não Funcionais](#requisitos-nao-funcionais)
   3. [Custos](#custos)
   4. [Outros Requisitos do Produto](#outros-requisitos-do-produto)
      - [Requisitos da Solução](#requisitos-da-solucao)
      - [Requisitos de Documentação](#requisitos-de-documentacao)
   5. [Riscos e Restrições](#riscos-e-restricoes)
      - [Riscos](#riscos)
      - [Restrições](#restricoes)
   6. [Documentos de Referência](#documentos-de-referencia)

---

### 1. Introdução <a name="introducao"></a>
Este documento tem por objetivo trazer clareza quanto à necessidade de desenvolver/implantar o sistema, Gestor de Carreiras feito pela Tec21, disponibilizando detalhes sobre as características-chave necessárias para o produto, partes interessadas, restrições e riscos, dentre outras informações relevantes para entendimento da necessidade e do que se pretende alcançar com o projeto.

### 2. Análise de Contexto <a name="analise-de-contexto"></a>
#### 2.1. Detalhamento da Necessidade <a name="detalhamento-da-necessidade"></a>
##### 2.1.1. Descrição do Problema <a name="descricao-do-problema"></a>
O problema a ser resolvido é a falta de um sistema para gerenciar carreiras. Integrando como ator principal o estudante, apresentando soluções de empregabilidade e planos de ação para desenvolvimento pessoal e profissional.

##### 2.1.2. Parte(s) Afetada(s) <a name="partes-afetadas"></a>
As áreas afetadas incluem o setor de Recursos Humanos das empresas parceiras, estudantes que buscam orientação e desenvolvimento de carreira, mentores que fornecem suporte e orientação, e administradores do sistema que gerenciam o funcionamento e a manutenção do sistema.

##### 2.1.3. Impacto <a name="impacto"></a>
A falta de um sistema integrado para gerenciar carreiras resulta em ineficiências na comunicação entre estudantes, empresas e mentores. Isso pode levar a oportunidades perdidas de emprego para os estudantes, dificuldades na gestão de candidatos para as empresas e desafios na monitorização e acompanhamento de mentorias.

##### 2.1.4. Solução de Sucesso <a name="solucao-de-sucesso"></a>
-Uma plataforma centralizada para o gerenciamento de carreiras que seja acessível para estudantes, empresas e mentores.

-Ferramentas de planejamento de carreira que ajudem os estudantes a definir metas e acompanhar seu progresso.

-Um sistema de mentoria que permita a conexão entre estudantes e mentores, facilitando o acompanhamento e feedback.

-Funcionalidades para empresas publicarem vagas e gerenciarem candidatos.

-Relatórios e dashboards que forneçam visões sobre o progresso dos estudantes e o desempenho das mentorias.


### 3. Partes Interessadas <a name="partes-interessadas"></a>
Instituições de ensino
empresas beneficentes
empresas
Estudantes
Especialistas


#### 3.1. Partes Interessadas <a name="lista-de-partes-interessadas"></a>
Lista todas as partes interessadas identificadas.

| Unidade     |           Representada por            | Envolvimento com o projeto |
| ------------| --------------------------------------| -------------------------- |
| RH Empresas | Representantes das empresas parceiras | Envolvimento direto na definição dos requisitos de vagas e gestão de candidatos |
| Alunos      | Representantes estudantis             | Envolvimento na definição das necessidades de orientação de carreira e mentoria |
| Mentores    | Representantes de mentores            | Envolvimento na definição dos processos de mentoria e acompanhamento de alunos  |

#### 3.2. Usuários <a name="usuarios"></a>


| Tipo do usuário | Representante(s) |                          Descrição                       | Responsabilidades |
| --------------- | ---------------- | -------------------------------------------------------- | ----------------- |
| Administrador   | Equipe de TI     | Gerencia todo o sistema, incluindo usuários e permissões | Manutenção do sistema, criação        de  usuários, gestão de permissões |

|       Aluno     |    Estudantes  | Usa o sistema para gerenciar seu plano de carreira e interagir com mentores | Criação e atualização de perfil, solicitação de mentoria |

| Empresa | RH | Usa o sistema para gerenciar vagas e candidatos | Criação e atualização de vagas, gestão de candidatos |

| Mentor | Especialistas | Usa o sistema para gerenciar seus mentorados e registrar sessões de mentoria | Acompanhamento de mentorados, registro de sessões de mentoria |

#### 3.3. Necessidades das Partes Interessadas ou Usuários <a name="necessidades-das-partes-interessadas-ou-usuarios"></a>
Tipo do usuário: Administrador
Representante(s): Gerente de TI, Auxiliar de TI, Equipe de desenvolvimento, Diretores, CEO’s
Descrição: Gerencia todo o sistema, incluindo usuários e permissões
Responsabilidades: Manutenção do sistema, criação de usuários, gestão de permissões

Tipo do usuário: Estudantes
Representante(s): Estudantes, Coordenadores, Professores
Descrição: Usa o sistema para gerenciar seu plano de carreira e interagir com mentores e vagas disponibilizadas pelas empresas
Responsabilidades: Criação e atualização de perfil, solicitação de mentoria e candidatura a vagas no sistema ou integrações

Tipo do usuário: Empresa
Representante(s): Setor RH
Descrição: Usa o sistema para gerenciar vagas e candidatos
Responsabilidades: Criação e atualização de vagas, gestão de candidatos

Tipo do usuário: Mentor
Representante(s): Direção da instituição
Descrição: Usa o sistema para gerenciar seus mentorados e registrar sessões de mentoria
Responsabilidades: Acompanhamento de mentorados, registro de sessões de mentoria

##### <Empresas> <a name="Empresas"></a>
Parte(s) Interessada(s): Setor de RH
Motivadores: Facilidade na criação de vagas e encontro de candidatos apropriados com as qualidades necessárias
Situação atual: Uso de plataformas de candidatura de vagas, recebimento de currículos diretos
Solução ideal: Identificação do candidato com a vaga e empresa, minimizando o atrito de interesses
##### <Estudantes> <a name="Estudantes"></a>
Motivadores: Busca pela carreira profissional ideal que seja bem remunerada e compatível com interesses
Situação atual: Informações volumosas e confusas, formulários extensos e complexos
Solução ideal: Agrupamento de informações, estabelecendo e sugerindo soluções pontuais que promovam a evolução e adaptação
##### <Mentores> <a name="Mentores"></a>
Motivadores: Possibilidade de desenvolver habilidades técnicas, especialização e participar do desenvolvimento direto dos estudantes
Situação atual: Inexistente
Solução ideal: Atuação direta com os alunos que requisitaram mentoria, disponibilizando experiência de aprendizagem, documentação para registro de instrução especializada

### 4. Objetivos de Negócio <a name="objetivos-de-negocio"></a>
Com base nas necessidades e expectativas das partes interessadas, identifique os objetivos de negócio que serão completadas ou parcialmente atendidos após a execução bem-sucedida do projeto.


### 5. Visão Geral do Produto <a name="visao-geral-do-produto"></a>
#### 5.1. Perspectiva do Produto <a name="perspectiva-do-produto"></a>
O sistema Gestor de Progressão de Carreira é uma plataforma integrada destinada a gerenciar carreiras e desenvolvimento profissional de estudantes. Ele interage com outros sistemas de gestão de Recursos Humanos das empresas parceiras e com plataformas de e-learning.

#### 5.2. Características-Chave do Produto <a name="caracteristicas-chave-do-produto"></a>
#### todos com prioridade ## Alta
- Gestão de Vagas: Proporciona ferramentas para que os alunos planejem suas carreiras, definindo metas e acompanhando seu progresso.
- Planejamento de Carreira: Proporciona ferramentas para que os alunos planejem suas carreiras, definindo metas e acompanhando seu progresso.
- Sistema de Mentoria: Facilita a conexão entre alunos e mentores, permitindo o acompanhamento e feedback das sessões de mentoria.
##### 5.2.1. Requisitos não Funcionais <a name="requisitos-nao-funcionais"></a>


#### 5.3. Custos <a name="custos"></a>
#### 5.4. Outros Requisitos do Produto <a name="outros-requisitos-do-produto"></a>
Em um alto nível, lista os padrões aplicáveis, os requisitos de hardware ou plataforma, os requisitos de desempenho e os requisitos ambientais.

##### 5.4.1. Requisitos da Solução <a name="requisitos-da-solucao"></a>
- Memória: Mínimo de 8gb de RAM para servidores
- Espaço de Armazenamento: Mínimo SSD de 256
- Processamento: Processador multi-core de 3.0 GHz ou superior

##### 5.4.2. Requisitos de Documentação <a name="requisitos-de-documentacao"></a>
- Documentação técnica: Disponivel em PDF
- Guia de usuário: Manual para uso de administradores, alunos empresas e mentores. formato Web.

#### 5.5. Riscos e Restrições <a name="riscos-e-restricoes"></a>
##### 5.5.1. Riscos <a name="riscos"></a>
Lista todos os riscos percebidos que podem impactar com o alcance do objetivo do projeto.

| Nome do Risco | Tipo do Risco | Probabilidade | Impacto |
| ------------- | ------------- | ------------- | ------- |
| Falta de adoção | Operacional | Média | Alto |
| Problemas de segurança | Técnico | Baixa | Alto |
| Atrasos no cronograma | Gerencial | Alta | Médio |

##### 5.5.2. Restrições <a name="restricoes"></a>
Lista todas as restrições de design, restrições externas, como requisitos operacionais ou regulamentares, ou outras dependências.

| Tipo | Nome | Descrição |
| ---- | ---- | --------- |
| Recursos Humanos | Equipe limitada | Disponibilidade limitada de desenvolvedores e administradores de sistema |
| Tempo | Prazo curto | Prazo de entrega do projeto em 6 meses |

#### 5.6. Documentos de Referência <a name="documentos-de-referencia"></a>
Lista todos os documentos aos quais o documento de visão faz referência. Identifique cada documento por título, número de relatório (se aplicável), data e organização de publicação. Especifique as origens a partir das quais os leitores podem obter as referências.

| Documento | Descrição | Acesso |
| --------- | --------- | ------ |
| Plano de Projeto | Detalha o plano de execução do projeto | Intranet |
| Especificação de Requisitos | Lista todos os requisitos funcionais e não funcionais | Repositório de documentos |

