from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "uptime" in data

def test_capabilities():
    response = client.get("/capabilities")
    assert response.status_code == 200
    data = response.json()
    assert "features" in data
    assert "udc_version" in data

def test_state():
    response = client.get("/state")
    assert response.status_code == 200
    data = response.json()
    assert "uptime_seconds" in data

def test_message():
    response = client.post("/message", json={"trace_id": "test-123", "payload": {}})
    assert response.status_code == 200
    data = response.json()
    assert data["received"] is True
    assert data["trace_id"] == "test-123"

