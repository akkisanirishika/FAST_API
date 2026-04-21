from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter()
todos: dict[int, dict[str, object]] = {}
next_todo_id = 1


class TodoCreate(BaseModel):
    title: str


class TodoUpdate(BaseModel):
    title: str
    done: bool


class TodoResponse(BaseModel):
    id: int
    title: str
    done: bool


@router.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello from FastAPI!"}


@router.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/todos", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(payload: TodoCreate) -> TodoResponse:
    global next_todo_id

    todo = {"id": next_todo_id, "title": payload.title, "done": False}
    todos[next_todo_id] = todo
    next_todo_id += 1
    return TodoResponse(**todo)


@router.get("/todos", response_model=list[TodoResponse])
def list_todos() -> list[TodoResponse]:
    return [TodoResponse(**todo) for todo in todos.values()]


@router.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int) -> TodoResponse:
    todo = todos.get(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return TodoResponse(**todo)


@router.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, payload: TodoUpdate) -> TodoResponse:
    todo = todos.get(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    updated_todo = {"id": todo_id, "title": payload.title, "done": payload.done}
    todos[todo_id] = updated_todo
    return TodoResponse(**updated_todo)


@router.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int) -> None:
    todo = todos.pop(todo_id, None)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")


def reset_todos() -> None:
    """Test helper to reset in-memory state."""
    global next_todo_id
    todos.clear()
    next_todo_id = 1
