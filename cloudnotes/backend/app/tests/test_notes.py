from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_and_list_note():
    create_resp = client.post(
        "/notes",
        json={"title": "hello", "content": "world"},
    )
    assert create_resp.status_code == 200

    note = create_resp.json()
    assert note["title"] == "hello"

    list_resp = client.get("/notes")
    assert list_resp.status_code == 200
    assert len(list_resp.json()) >= 1
    
    
def test_delete_note():
    create_resp = client.post(
        "/notes",
        json={"title": "tmp", "content": "delete me"},
    )
    note_id = create_resp.json()["id"]

    delete_resp = client.delete(f"/notes/{note_id}")
    assert delete_resp.status_code == 200