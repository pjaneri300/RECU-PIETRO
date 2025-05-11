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
        ├── projeto9.png
        └── projeto10.png


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


## 🚓Imagens do sistema funcionando

1-**Homepage**

![projeto](https://github.com/user-attachments/assets/ed681682-b22c-42b3-91d7-15d381f78a32)

2-**Novo projeto**

![projeto2](https://github.com/user-attachments/assets/765a36b7-3671-4a52-9e7b-73e01fefe088)

3-**Homepage com o projeto já existente**

![Projeto3](https://github.com/user-attachments/assets/8c7ea331-ac7c-4334-8bee-3e801dbe043c)

4-**Interface de edição do projeto**

![projeto4](https://github.com/user-attachments/assets/300c280e-88b7-4099-a268-3db0e109493b)

5-**Interface com projeto editado**

![projeto5](https://github.com/user-attachments/assets/7387692e-a66d-49eb-b7d3-d77c92cc3d70)


6-**Interface da criação de tarefas**

![projeto6](https://github.com/user-attachments/assets/df364b0e-1ec4-4969-b58a-9a5821de9780)

7-**Criação de uma nova tarefa**


![projeto7](https://github.com/user-attachments/assets/933b17cb-9557-4bb7-ad35-fccf89e3d699)

8-**Interface já com a tarefa criada**


![projeto8](https://github.com/user-attachments/assets/59e37104-190d-4377-b1b4-160d8016a69a)

9-**Interface de edição de tarefas**

![projeto9](https://github.com/user-attachments/assets/9ec03399-e239-4b1a-a7b8-da74dc64bad2)

10-**Interface com a tarefa editada**

![projeto10](https://github.com/user-attachments/assets/a7d73125-6a55-43e3-aa82-0456e282e3e2)


11-**Interface com a tarefa excluida**

![projeto5](https://github.com/user-attachments/assets/2af0f53c-2e66-494c-a7d9-e0e3d3488874)

12-**Homepage com o projeto excluido**

![projeto](https://github.com/user-attachments/assets/19b71ef4-b27a-40d0-99ee-0c15d2b8127c)






