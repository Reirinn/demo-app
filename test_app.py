from app import app

def test_home():
    client = app.test_client()
    assert client.get("/").status_code == 200