from fastapi.testclient import TestClient

from app.api.routes import reset_todos
from app.main import app

client = TestClient(app)


def setup_function() -> None:
    reset_todos()


def test_read_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI!"}


def test_health_check() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_todo_crud_flow() -> None:
    create_response = client.post("/todos", json={"title": "Learn FastAPI"})
    assert create_response.status_code == 201
    created_todo = create_response.json()
    assert created_todo == {"id": 1, "title": "Learn FastAPI", "done": False}

    list_response = client.get("/todos")
    assert list_response.status_code == 200
    assert list_response.json() == [created_todo]

    get_response = client.get("/todos/1")
    assert get_response.status_code == 200
    assert get_response.json() == created_todo

    update_response = client.put("/todos/1", json={"title": "Learn FastAPI well", "done": True})
    assert update_response.status_code == 200
    assert update_response.json() == {"id": 1, "title": "Learn FastAPI well", "done": True}

    delete_response = client.delete("/todos/1")
    assert delete_response.status_code == 204

    missing_response = client.get("/todos/1")
    assert missing_response.status_code == 404
    assert missing_response.json() == {"detail": "Todo not found"}
