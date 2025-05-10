from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

PROJECTS_FILE = 'projetos.csv'
TASKS_FILE = 'tarefas.csv'

if not os.path.exists(PROJECTS_FILE):
    with open(PROJECTS_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'nome', 'descricao'])

if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'projeto_id', 'nome', 'status'])

def read_projects():
    projects = []
    with open(PROJECTS_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            projects.append(row)
    return projects

def read_tasks():
    tasks = []
    with open(TASKS_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tasks.append(row)
    return tasks

def write_project(project):
    projects = read_projects()
    with open(PROJECTS_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        project_id = len(projects) + 1
        writer.writerow([project_id, project['nome'], project['descricao']])

def update_projects(projects):
    with open(PROJECTS_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'nome', 'descricao'])
        for p in projects:
            writer.writerow([p['id'], p['nome'], p['descricao']])

def write_task(task):
    tasks = read_tasks()
    with open(TASKS_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        task_id = len(tasks) + 1
        writer.writerow([task_id, task['projeto_id'], task['nome'], task['status']])

def update_tasks(tasks):
    with open(TASKS_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'projeto_id', 'nome', 'status'])
        for t in tasks:
            writer.writerow([t['id'], t['projeto_id'], t['nome'], t['status']])

def find_project(projects, project_id):
    for p in projects:
        if int(p['id']) == project_id:
            return p
    return None

def find_task(tasks, tarefa_id):
    for t in tasks:
        if int(t['id']) == tarefa_id:
            return t
    return None

@app.route('/')
def index():
    projects = read_projects()
    return render_template('index.html', projects=projects)

@app.route('/projeto/<int:projeto_id>')
def projeto(projeto_id):
    projects = read_projects()
    tasks = [task for task in read_tasks() if int(task['projeto_id']) == projeto_id]
    project = find_project(projects, projeto_id)
    return render_template('projeto.html', project=project, tasks=tasks)

@app.route('/novo_projeto', methods=['GET', 'POST'])
def novo_projeto():
    if request.method == 'POST':
        project = {'nome': request.form['nome'], 'descricao': request.form['descricao']}
        write_project(project)
        return redirect(url_for('index'))
    return render_template('novo_projeto.html')

@app.route('/editar_projeto/<int:projeto_id>', methods=['GET', 'POST'])
def editar_projeto(projeto_id):
    projects = read_projects()
    project = find_project(projects, projeto_id)
    if request.method == 'POST':
        project['nome'] = request.form['nome']
        project['descricao'] = request.form['descricao']
        update_projects(projects)
        return redirect(url_for('index'))
    return render_template('editar_projeto.html', project=project)

@app.route('/excluir_projeto/<int:projeto_id>', methods=['POST'])
def excluir_projeto(projeto_id):
    projects = read_projects()
    tasks = read_tasks()
   
    tasks = [t for t in tasks if int(t['projeto_id']) != projeto_id]
  
    projects = [p for p in projects if int(p['id']) != projeto_id]
  
    update_projects(projects)
    update_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/nova_tarefa/<int:projeto_id>', methods=['GET', 'POST'])
def nova_tarefa(projeto_id):
    if request.method == 'POST':
        task = {
            'projeto_id': projeto_id,
            'nome': request.form['nome'],
            'status': request.form['status']
        }
        write_task(task)
        return redirect(url_for('projeto', projeto_id=projeto_id))
    return render_template('nova_tarefa.html', projeto_id=projeto_id)

@app.route('/editar_tarefa/<int:tarefa_id>', methods=['GET', 'POST'])
def editar_tarefa(tarefa_id):
    tasks = read_tasks()
    task = find_task(tasks, tarefa_id)
    if request.method == 'POST':
        task['nome'] = request.form['nome']
        task['status'] = request.form['status']
        update_tasks(tasks)
        return redirect(url_for('projeto', projeto_id=task['projeto_id']))
    return render_template('editar_tarefa.html', task=task)

@app.route('/excluir_tarefa/<int:tarefa_id>', methods=['POST'])
def excluir_tarefa(tarefa_id):
    tasks = read_tasks()
    task = find_task(tasks, tarefa_id)
    if task:
        tasks = [t for t in tasks if int(t['id']) != tarefa_id]
        update_tasks(tasks)
    return redirect(url_for('projeto', projeto_id=task['projeto_id']) if task else url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)