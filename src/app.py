from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

# Simulando banco de dados em memória
tarefas = []
contador_id = 1

@app.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)

@app.route('/criar', methods=['POST'])
def criar():
    global contador_id
    titulo = request.form.get('titulo')
    descricao = request.form.get('descricao')
    
    tarefas.append({
        'id': contador_id,
        'titulo': titulo,
        'descricao': descricao,
        'status': 'To Do'
    })
    contador_id += 1
    return redirect(url_for('index'))

@app.route('/atualizar/<int:task_id>/<novo_status>')
def atualizar(task_id, novo_status):
    for t in tarefas:
        if t['id'] == task_id:
            t['status'] = novo_status
            break
    return redirect(url_for('index'))

@app.route('/deletar/<int:task_id>')
def deletar(task_id):
    global tarefas
    tarefas = [t for t in tarefas if t['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)