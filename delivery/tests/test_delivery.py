from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_list_deliveries():
    response = client.get("/deliveries")
    assert response.status_code == 200
    assert response.json()["deliveries_count"] == len(response.json()["deliveries"])
