import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_enviar_arquivo_cnab():
    """Testa se a API aceita um arquivo CNAB"""
    
    with open("tests/mock_cnab.txt", "rb") as file:
        response = client.post("/cnab/enviar_cnab", files={"file": file})
    
    assert response.status_code == 201
    assert "mensagem" in response.json()

def test_buscar_transacoes():
    """Testa se a API retorna as transações corretamente"""
    
    response = client.get("/cnab/consultar_cnab")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Esperamos uma lista de transações
