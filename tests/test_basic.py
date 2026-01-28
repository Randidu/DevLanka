from fastapi.testclient import TestClient
from app import create_app

client = TestClient(create_app())

def test_read_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
