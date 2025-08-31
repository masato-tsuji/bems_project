from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_hello():
    res = client.get("/hello")
    assert res.status_code == 200
    assert res.json() == {"message": "Hello from FastAPI backend!"}
