import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as c:
        yield c

def test_index_status(client):
    r = client.get("/")
    assert r.status_code == 200

def test_index_contains_table(client):
    r = client.get("/")
    assert b"Tabla de posiciones" in r.data or b"Tabla de posiciones - Liga Pro" in r.data
