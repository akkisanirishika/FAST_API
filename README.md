# Beginner FastAPI Project

This is a minimal FastAPI starter project with:

- virtual environment (`venv`) setup
- clean folder structure
- route-based API structure
- two basic `GET` endpoints (`/` and `/health`)
- Todo CRUD API (`/todos`)
- basic test setup with `pytest`
- run instructions using `uvicorn`

## Project Structure

```text
FAST_API/
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  └─ api/
│     ├─ __init__.py
│     └─ routes.py
├─ requirements.txt
├─ requirements-dev.txt
├─ tests/
│  └─ test_main.py
└─ README.md
```

## 1) Create and Activate Virtual Environment (Windows PowerShell)

From the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If script execution is blocked, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 2) Install Dependencies

```powershell
pip install -r requirements.txt
```

Optional dev tools:

```powershell
pip install -r requirements-dev.txt
```

## 3) Run the App with Uvicorn

```powershell
uvicorn app.main:app --reload
```

Server starts at:

- API: `http://127.0.0.1:8000/`
- Swagger docs: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Endpoints Included

### `GET /`

Returns:

```json
{
  "message": "Hello from FastAPI!"
}
```

### `GET /health`

Returns:

```json
{
  "status": "ok"
}
```

### Todo API

- `POST /todos` create a todo
- `GET /todos` list todos
- `GET /todos/{todo_id}` get one todo
- `PUT /todos/{todo_id}` update title and done state
- `DELETE /todos/{todo_id}` delete a todo

## 4) Run Tests

```powershell
pytest -q
```

## 5) Run Lint Check (Optional)

```powershell
ruff check .
```

