from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_chat():
    response = client.post("/chat/", json={"message": "Hello", "history": []})
    assert response.status_code == 200
    assert "response" in response.json()
