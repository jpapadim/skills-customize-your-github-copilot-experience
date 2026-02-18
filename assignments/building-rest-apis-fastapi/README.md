# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using the FastAPI framework. You'll define request/response models with Pydantic and implement CRUD endpoints for a simple in-memory resource.

## 📝 Tasks

### 🛠️ Create a FastAPI Service

#### Description

Implement a FastAPI application that exposes endpoints to create, read, update, and delete `Item` resources. Use Pydantic models for validation and an in-memory store (dictionary) for persistence.

#### Requirements
Completed program should:

- Define a Pydantic model `Item` with `id: int`, `name: str`, and `price: float`
- Implement endpoints:
  - `GET /items/` — list items
  - `GET /items/{id}` — retrieve a single item
  - `POST /items/` — create a new item
  - `PUT /items/{id}` — update an existing item
  - `DELETE /items/{id}` — delete an item
- Validate incoming data and return appropriate HTTP status codes
- Use an in-memory dictionary to store items for the duration of the server run

## 🚀 Stretch Goals (optional)

- Add query parameters for filtering or pagination
- Persist data to a simple JSON file
- Add OpenAPI examples and more detailed response models

## 🧾 How to run

Create a virtual environment, install dependencies, and start the app with Uvicorn:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r assignments/building-rest-apis-fastapi/requirements.txt
uvicorn assignments.building_rest_apis_fastapi.starter_app:app --reload --port 8000
```

Then open `http://localhost:8000/docs` to view the interactive API docs.

## 🧠 Learning Outcomes

- Understand FastAPI app structure and routing
- Use Pydantic models for validation and serialization
- Implement basic RESTful endpoints and proper HTTP codes

## 📚 Resources

- FastAPI docs: https://fastapi.tiangolo.com/
- Pydantic docs: https://pydantic-docs.helpmanual.io/
