from fastapi.testclient import TestClient
import sys
from pathlib import Path
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/livez")
    assert response.status_code == 200
    assert response.json() == {"status": "app is running"}