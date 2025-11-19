# 📝 To-Do List Project (Django + REST API + Templates)

A complete **To-Do List Web Application** built using **Django**, featuring REST APIs, HTML templates, JavaScript integration, and SQLite database storage.  
This project follows a clean, scalable folder structure and supports Docker-based deployment.

---

## 🚀 Features Overview

### 🔹 API Features (REST)
- Create new tasks  
- List all tasks  
- Retrieve single task  
- Update existing task  
- Delete task (**200 OK**)  
- JSON-formatted responses  

### 🔹 Frontend Features (Templates + JS)
- Display tasks in a dynamic table  
- Add new tasks  
- Edit tasks  
- Delete tasks  
- Fully powered by JavaScript (Fetch API)

### 🔹 Engineering Highlights
- SQLite database + raw SQL service layer  
- Separate **API Views** and **Template Views**  
- `TaskService` for DB operations  
- Clean HTML templates  
- CSRF-protected forms  
- Fully testable with pytest  

---

# 📦 Project Structure

```
todo_project/
│── tasks/
│   ├── templates/tasks/
│   ├── static/
│   ├── services/
│   ├── api_views.py
│   ├── web_views.py
│   └── models.py
│
│── todo_project/
│── tests/
│── requirements.txt
│── Dockerfile
│── docker-compose.yml
│── manage.py
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone git@github.com:Gauravmehra59/todo_project.git
cd todo_project
```

---

# 🐳 Running With Docker (Recommended)

```bash
docker-compose up --build
```

Visit:

👉 http://127.0.0.1:8000/

---

# 🖥 Running Locally (Without Docker)

## 2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

## 3️⃣ Apply Migrations

```bash
python manage.py migrate
```

## 4️⃣ Start Django Server

```bash
python manage.py runserver
```

Open:

👉 http://127.0.0.1:8000/

---

# 📮 API Endpoints (JSON)

### ✔ List All Tasks
```http
GET /api/list/
```

### ✔ Get Single Task
```http
GET /api/detail/<id>/
```

### ✔ Create Task
```http
POST /api/create/
```

#### Example Body
```json
{
  "title": "Buy Eggs",
  "description": "6 eggs",
  "due_date": "2025-11-21",
  "status": "pending"
}
```

### ✔ Update Task
```http
PATCH /api/update/<id>/
```

### ✔ Delete Task
```http
DELETE /api/delete/<id>/
```

---

# 🧪 Running Test Cases

Run all test cases:

```bash
pytest -v
```

---

# 🛠 Tech Stack

- Python 3.12
- Django
- HTML / CSS / JavaScript
- SQLite
- Docker + Docker Compose
- Pytest

---

# ❤️ Author

**Gaurav Mehra**  
Software Developer
