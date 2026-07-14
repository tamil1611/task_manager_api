# Task Manager API

A simple RESTful Task Manager API built with **FastAPI**, **SQLite**, **SQLAlchemy**, and **Pydantic**. This project demonstrates CRUD (Create, Read, Update, Delete) operations for managing tasks.

## Features

* Create a task
* View all tasks
* Update an existing task
* Delete a task
* SQLite database integration
* SQLAlchemy ORM
* Pydantic request validation
* Interactive Swagger API documentation

## Tech Stack

* **Backend:** Python, FastAPI
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Validation:** Pydantic
* **Server:** Uvicorn

## Project Structure

```text
task-manager/
│── main.py
│── database.py
│── models.py
│── schemas.py
│── crud.py
│── requirements.txt
│── README.md
└── tasks.db
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd task-manager
```

2. Create a virtual environment (optional but recommended):

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:

```bash
uvicorn main:app --reload
```

The application will be available at:

* API: http://127.0.0.1:8000
* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint      | Description         |
| ------ | ------------- | ------------------- |
| POST   | `/tasks`      | Create a new task   |
| GET    | `/tasks`      | Retrieve all tasks  |
| PUT    | `/tasks/{id}` | Update a task by ID |
| DELETE | `/tasks/{id}` | Delete a task by ID |

## Request Example

### Create Task

**POST** `/tasks`

```json
{
  "title": "Learn FastAPI",
  "description": "Complete CRUD assignment",
  "status": "Pending"
}
```

### Success Response

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Complete CRUD assignment",
  "status": "Pending"
}
```

## Database

This project uses **SQLite** as the database. The database file (`tasks.db`) is automatically created when the application starts.

## Validation

Each task contains the following fields:

* **title** (string)
* **description** (string)
* **status** (`Pending` or `Completed`)

## Future Improvements

* Search tasks
* Filter by status
* Pagination
* Authentication and authorization
* Docker support
* Unit tests
* Task due dates and priorities

## Author

Developed as a FastAPI CRUD assignment demonstrating REST API development with Python, FastAPI, SQLAlchemy, SQLite, and Pydantic.
