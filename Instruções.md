# Instruções

Lista de instruções úteis para os desenvolvedores.

<br>

### 🍴 Criar um novo Fork
- Acessar a página do repositório original no Github
- Clicar no botão Fork no canto superior direito da página
- Na janela de detalhes sobre o Fork criado, selecione a opção de "puxar" todas as branch's do repositório
- Na página do seu Fork, clicar no botão Code e copiar o link do seu repositório
- Abrir o Git Bash na pasta onde você deseja iniciar o projeto
- Caso não esteja conectado, conecte sua conta do Github
- Dê <code>git clone [link]</code> para baixar todo o repositório do projeto
- Rode o comando <code>pip install -r requirements.txt</code> para instalar as bibliotecas necessárias

<br>

### ⚡ Atualizar a lista de bibliotecas

Após baixar um novo pacote para o projeto, siga esses passos:
1. Abrir a pasta "gestordecarreiras" no terminal
2. Rodar o código <code>pip freeze > requirements.txt</code>


<br>

### 🎯 Enviar suas alterações

Antes de fazer suas alterações e enviá-las para o seu fork, devemos puxar a versão mais atual do código. Passo a passo:

- Sincronizar o seu fork com o repositório original pelo Github
- Abrir a pasta do projeto no Git Bash
- Atualizar o código do seu computador com o comando <code>git pull</code>
- Mudar para a branch que está sendo trabalhada com o comando <code>git checkout [nome_da_branch]</code>
- Após fazer as alterações, elas devem ser enviadas para o commit com o comando <code>git add .</code> 
- Deve ser realizado o commit com o comando <code>git commit -m "mensagem padronizada"</code>
- Em seguida devemos enviar os commits para o Github com o comando <code>git push origin [nome_da_branch]</code>
- No Github deve ser feito o pedido de Pull Request

<br>

### 📌 Padrão de Commits

Os commits do projeto serão realizados seguindo as recomendações estabelecidas a baixo:
<table>
  <thead>
    <tr>
        <th>Palavra-Chave</th>
        <th>Tipo de Commit</th>
        <th>Exemplo</th>
    </tr>
  </thead>
 <tbody>
    <tr>
        <td><code>Feat</code></td>
        <td>Inserindo novas features</td>
        <td><b>Feat:</b> added click on button "send"</td>
    </tr>
    <tr>
        <td><code>Update</code></td>
        <td>Alterações ou atualizações no código</td>
        <td><b>Update:</b> class Aluno</td>
    </tr>
    <tr>
        <td><code>Docs</code></td>
        <td>Mudanças na documentação</td>
        <td><b>Docs:</b> update on README.md</td>
    </tr>
    <tr>
        <td><code>Fix</code></td>
        <td>Consertando bugs</td>
        <td><b>Fix:</b> remove infinite loop on line 50</td>
    </tr>
    <tr>
        <td><code>Remove</code></td>
        <td>Removendo features, arquivos ou pastas</td>
        <td><b>Remove:</b> folder "images"</td>
    </tr>
    <tr>
        <td><code>Cleanup</code></td>
        <td>Limpeza do código, remoção de comentários</td>
        <td><b>Cleanup:</b> unnecessary comments and variables</td>
    </tr>
  </tbody>
</table>