import pytest
from app import app

@pytest.fixture
def client():
    """
    Configuração do cliente de teste do Flask.

    Desafio Extra:
    Implementar testes automatizados para a API Flask
    utilizando o framework pytest.
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_soma(client):
    """Valida se o endpoint de soma retorna o valor esperado."""
    response = client.get("/soma?a=3&b=7")
    assert response.status_code == 200
    assert response.get_json()["resultado"] == 10

def test_divisao(client):
    """Valida se o endpoint de divisão retorna o valor correto."""
    response = client.get("/divisao?a=10&b=2")
    assert response.status_code == 200
    assert response.get_json()["resultado"] == 5

def test_divisao_por_zero(client):
    """Confirma que a divisão por zero resulta em resposta de erro adequada."""
    response = client.get("/divisao?a=10&b=0")
    assert response.status_code == 400
    assert "erro" in response.get_json()
