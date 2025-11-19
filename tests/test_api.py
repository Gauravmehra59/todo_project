import json
import pytest
from django.test import Client
from django.db import connection

client = Client()


def create_tasks_table():
    with connection.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                due_date TEXT NOT NULL,
                status TEXT NOT NULL
            );
        """)


# Helper function to clean DB before each test
def reset_tasks_table():
    with connection.cursor() as cur:
        cur.execute("DELETE FROM tasks")


# Before each test clear table
@pytest.fixture(autouse=True)
def run_before_each():
    create_tasks_table()
    reset_tasks_table()
    yield
    reset_tasks_table()


# TEST: Create Task API
@pytest.mark.django_db
def test_create_task():
    payload = {
        "title": "Test Task",
        "description": "Testing description",
        "due_date": "2025-11-20",
        "status": "pending"
    }

    response = client.post(
        "/api/create/",
        data=json.dumps(payload),
        content_type="application/json"
    )

    assert response.status_code == 201
    data = response.json()
    assert data["message"] == "Task created successfully"


# TEST: Get Task List
@pytest.mark.django_db
def test_list_tasks():
    # Insert manually
    with connection.cursor() as cur:
        cur.execute("""
        INSERT INTO tasks (title, description, due_date, status)
        VALUES ('Sample', 'Desc', '2025-11-20', 'pending')
        """)

    response = client.get("/api/list/")

    assert response.status_code == 200
    data = response.json()

    assert len(data["tasks"]) == 1
    assert data["tasks"][0]["title"] == "Sample"


# TEST: Get Task Details
@pytest.mark.django_db
def test_task_detail():
    with connection.cursor() as cur:
        cur.execute("""
        INSERT INTO tasks (title, description, due_date, status)
        VALUES ('Detail Task', 'Desc', '2025-11-20', 'pending')
        """)

        task_id = cur.lastrowid

    response = client.get(f"/api/detail/{task_id}/")

    assert response.status_code == 200
    data = response.json()

    assert data["title"] == "Detail Task"


# TEST: Update Task
@pytest.mark.django_db
def test_update_task():
    with connection.cursor() as cur:
        cur.execute("""
        INSERT INTO tasks (title, description, due_date, status)
        VALUES ('Old Title', 'Old Desc', '2025-11-20', 'pending')
        """)
        task_id = cur.lastrowid

    updated_data = {
        "title": "New Title",
        "description": "Updated",
        "due_date": "2025-11-21",
        "status": "done"
    }

    response = client.put(
        f"/api/update/{task_id}/",
        data=json.dumps(updated_data),
        content_type="application/json"
    )

    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Task updated successfully"

    # Verify in DB
    with connection.cursor() as cur:
        cur.execute("SELECT title, status FROM tasks WHERE id=%s", [task_id])
        row = cur.fetchone()
        assert row[0] == "New Title"
        assert row[1] == "done"


# TEST: Delete Task
@pytest.mark.django_db
def test_delete_task():
    with connection.cursor() as cur:
        cur.execute("""
        INSERT INTO tasks (title, description, due_date, status)
        VALUES ('Delete Me', 'Desc', '2025-11-20', 'pending')
        """)
        task_id = cur.lastrowid

    response = client.delete(f"/api/delete/{task_id}/")

    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Task deleted successfully"

    # DB verify
    with connection.cursor() as cur:
        cur.execute("SELECT * FROM tasks WHERE id=%s", [task_id])
        assert cur.fetchone() is None
