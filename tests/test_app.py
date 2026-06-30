import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from app import app, tarefas

@pytest.fixture
def client():
    app.config['TESTING'] = True
    tarefas.clear()
    with app.test_client() as client:
        yield client

def test_criar_tarefa(client):
    resposta = client.post('/criar', data={'titulo': 'Aprender Git', 'descricao': 'Estudar branches'})
    assert resposta.status_code == 302
    assert len(tarefas) == 1
    assert tarefas[0]['titulo'] == 'Aprender Git'