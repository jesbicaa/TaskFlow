import pytest
from app import app, repo

@pytest.fixture
def client():
    app.config['TESTING'] = True
    repo.tarefas.clear()
    repo.contador_id = 1
    with app.test_client() as client:
        yield client

def test_fluxo_registro_tarefa(client):
    """Garante que a rota de criação responde com redirecionamento e adiciona o objeto no repositório."""
    resposta = client.post('/criar', data={
        'titulo': 'Carregamento Docas 3',
        'descricao': 'Separação de paletes para rota Sul',
        'prioridade': 'Alta'
    })
    assert resposta.status_code == 302
    lista = repo.listar()
    assert len(lista) == 1
    assert lista[0].titulo == 'Carregamento Docas 3'
    assert lista[0].prioridade == 'Alta'
    assert lista[0].status == 'To Do'