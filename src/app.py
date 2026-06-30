import os
import sys
from flask import Flask, render_template, request, redirect, url_for

# Configura o caminho de busca para evitar erros de importação nos testes
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

app = Flask(__name__, template_folder='templates')

class Task:
    """Classe que representa a entidade de uma tarefa conforme a modelagem UML."""
    def __init__(self, task_id, titulo, descricao, prioridade="Media", status="To Do"):
        self.id = task_id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade  # Inserido após mudança de escopo
        self.status = status

class TarefaRepository:
    """Repositório em memória simulando o banco de dados do sistema."""
    def __init__(self):
        self.tarefas = []
        self.contador_id = 1

    def listar(self):
        return self.tarefas

    def buscar_por_id(self, task_id):
        for t in self.tarefas:
            if t.id == task_id:
                return t
        return None

    def salvar(self, titulo, descricao, prioridade="Media"):
        nova_task = Task(self.contador_id, titulo, descricao, prioridade)
        self.tarefas.append(nova_task)
        self.contador_id += 1
        return nova_task

    def deletar(self, task_id):
        antes = len(self.tarefas)
        self.tarefas = [t for t in self.tarefas if t.id != task_id]
        return len(self.tarefas) < antes

repo = TarefaRepository()

@app.route('/')
def index():
    return render_template('index.html', tarefas=repo.listar())

@app.route('/criar', methods=['POST'])
def criar():
    titulo = request.form.get('titulo')
    descricao = request.form.get('descricao')
    prioridade = request.form.get('prioridade', 'Media') # Captura a nova feature de escopo
    repo.salvar(titulo, descricao, prioridade)
    return redirect(url_for('index'))

@app.route('/atualizar/<int:task_id>/<novo_status>')
def atualizar(task_id, novo_status):
    task = repo.buscar_por_id(task_id)
    if task:
        task.status = novo_status
    return redirect(url_for('index'))

@app.route('/deletar/<int:task_id>')
def deletar(task_id):
    repo.deletar(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)