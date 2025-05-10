## ✈ Gerenciador de Projetos

**Descrição Do Projeto:**

Este é um sistema web de gerenciamento de projetos desenvolvido com **Flask**. Ele permite que os usuários possam criar, editar, visualizar e excluir projetos, além de gerenciar tarefas associadas a cada projeto. As tarefas podem ser adicionadas, editadas, excluídas e categorizadas por status (**Pendente, Em Andamento, Concluído**). Os dados são armazenados em **arquivos CSV** (projetos.csv e tarefas.csv), e o frontend utiliza HTML com Tailwind CSS para uma interface moderna, responsiva e amigável.

## 🛴 Funcionalidades Implementadas

**Cadastrar Projetos:** Crie projetos com nome e descrição.

**Listar Projetos:** Visualize todos os projetos em uma interface de cartões.

**Editar Projetos:** Modifique nome e descrição de projetos existentes.

**Excluir Projetos:** Exclua projetos existentes.

**Adicionar Tarefas aos Projetos:** Adicione tarefas com nome e status.

**Editar e Remover Tarefas:** Atualize ou exclua tarefas de um projeto.

**Visualizar Tarefas de um Projeto:** Veja todas as tarefas associadas a um projeto específico.

**Armazenamento:** Utiliza arquivos CSV para persistência de dados.

## 🚤 Requisitos Técnicos

**Backend:** Flask (framework Python)

**Frontend:** HTML com Tailwind CSS (via CDN)

**Armazenamento:** Arquivos CSV (projetos.csv e tarefas.csv)

**Rotas:** Organizadas de forma simples e funcional

🚗 Estrutura do Projeto

```
gerenciador-projetos-tarefas/
│
├── app.py
├── projetos.csv
├── tarefas.csv
│
├── templates/
│   ├── index.html
│   ├── projeto.html
│   ├── novo_projeto.html
│   ├── editar_projeto.html
│   ├── nova_tarefa.html
│   └── editar_tarefa.html
│
└── static/
    └── img/
        ├── projeto1.png
        ├── projeto2.png
        ├── projeto3.png
        ├── projeto4.png
        ├── projeto5.png
        ├── projeto6.png
        ├── projeto7.png
        ├── projeto8.png
        └── projeto9.png

```


## 🚅 Instruções de Instalação e Execução

1-**Clonar o Repositório** (se aplicável):

```
git clone <URL_DO_REPOSITORIO>

cd gerenciador_projetos
```

Alternativamente, copie os arquivos para um diretório local.

2-**Criar e Ativar um Ambiente Virtual** (opcional, mas recomendado):

```
python -m venv venv

venv\Scripts\activate
```
**Instalar Dependências**: pip install flask


**Executar o Projeto:** python app.py

**Acessar o Sistema:** Abra o navegador e acesse http://127.0.0.1:5000/.

## 🚒 Exemplos de Uso


### **Listar e Gerenciar Projetos:**

Acesse a página inicial (/) para ver todos os projetos em um layout de cartões.

Clique em "Ver Projeto" para visualizar detalhes e tarefas , em "Editar" para modificar nome e descrição, ou em "Excluir" para exclui-lo.


### **Gerenciar Tarefas:**

Na página de um projeto, clique em "Nova Tarefa" para adicionar uma tarefa com nome e status.

Edite ou exclua tarefas usando os links "Editar" e "Excluir" ao lado de cada tarefa.


### **Observações**

A interface utiliza um esquema de cores roxo e branco.

Os arquivos CSV (projetos.csv e tarefas.csv) são criados automaticamente na primeira execução, se não existirem.

Certifique-se de que o diretório do projeto tenha permissões de escrita para manipulação dos arquivos CSV.

A funcionalidade de remover projetos não foi implementada no código fornecido.

## 🚓Imagens do sistema funcionando




