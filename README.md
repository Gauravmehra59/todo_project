# 📝 To-Do List Project (Django + REST API + Templates)

A complete **To-Do List Web Application** built with **Django**, featuring REST APIs, HTML templates, JavaScript-based interactions, and SQLite database storage.  
The project follows a clean, scalable architecture and also supports Docker-based deployment.

---

# ⚠️ Important Project Note (Please Read)

This project was intentionally built using **APIs and raw SQL** as part of the assignment requirements.

Because the goal was to emphasize API usage, I made sure to:

- Fetch data **exclusively through APIs**, even in places where Django templates could have supplied the data directly.
- For example, on the **Task List View**, instead of passing task data through the Django context, the HTML page is rendered first and then populated through a **Fetch API request**.
- Although many features could have been implemented more simply without APIs, the project was **designed to remain API-driven**, ensuring consistency with the assignment objectives.

This design choice is **intentional** to demonstrate proper API-first architecture.

---

# 🚀 Key Features

### 🔹 REST API Features
- Create new tasks  
- Retrieve task list  
- Retrieve a single task  
- Update tasks using **PATCH**  
- Delete tasks (**200 OK**)  
- JSON-formatted responses  

### 🔹 Frontend (Templates + JavaScript)
- Dynamic HTML table for displaying tasks  
- Add, edit, and delete tasks  
- Fully powered by **Fetch API**  
- API-driven UI without server-side data passing  

### 🔹 Engineering Highlights
- SQLite database using **raw SQL service layer**  
- Clear separation of **API Views** and **Template Views**  
- Central `TaskService` for all database operations  
- Clean, maintainable HTML templates  
- CSRF-protected forms  
- Fully testable with Pytest  

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

## 1️⃣ Clone the Repository

```bash
git clone git@github.com:Gauravmehra59/todo_project.git
cd todo_project
```

---

# 🐳 Run Using Docker (Recommended)

```bash
docker-compose up --build
```

Access the application at:

👉 http://127.0.0.1:8000/

---

# 🖥 Run Locally (Without Docker)

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 3️⃣ Apply Database Migrations

```bash
python manage.py migrate
```

## 4️⃣ Start Development Server

```bash
python manage.py runserver
```

Open in browser:

👉 http://127.0.0.1:8000/

---

# 📮 API Endpoints

### ✔ Get All Tasks
```http
GET /api/list/
```

### ✔ Get Task Details
```http
GET /api/detail/<id>/
```

### ✔ Create New Task
```http
POST /api/create/
```

#### Request Example
```json
{
  "title": "Buy Eggs",
  "description": "6 eggs",
  "due_date": "2025-11-21",
  "status": "pending"
}
```

### ✔ Update Existing Task
```http
PATCH /api/update/<id>/
```

### ✔ Delete Task
```http
DELETE /api/delete/<id>/
```

---

# 🧪 Running Tests

Run all tests using:

```bash
pytest -v
```

---

# 🛠 Tech Stack

- Python 3.12  
- Django  
- HTML / CSS / JavaScript  
- SQLite  
- Docker & Docker Compose  
- Pytest  

---

# ❤️ Author

**Gaurav Mehra**  
Software Developer  
