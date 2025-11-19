# 📝 To-Do List Project (Django + REST API + Templates)

A complete **To-Do List Web Application** built with **Django**, featuring REST APIs, HTML templates, JavaScript-based interactions, and SQLite database storage.  
The project follows a clean, scalable architecture and fully supports Docker-based deployment.

---

# ⚠️ Important Project Note (Please Read)

This project was intentionally developed using **APIs and raw SQL** to meet the assignment requirements.

To strictly follow an **API-first architecture**, I ensured the following:

- All data is fetched **only through APIs**, even in places where Django templates could have passed data directly.
- For the **Task List View**, instead of rendering task data using Django context, the page loads first and then fetches tasks using a **Fetch API GET request**.
- Although some features could have been implemented more easily without APIs, the goal of this assignment was to demonstrate **complete API integration** throughout the project.

This design choice is **100% intentional** to illustrate clean API-driven development.

---

# 🚀 Key Features

### 🔹 REST API Features
- Create new tasks  
- Retrieve all tasks  
- Retrieve a single task  
- Update tasks via **PATCH**  
- Delete tasks (**200 OK**)  
- Clean JSON-formatted responses  

### 🔹 Frontend (Templates + JavaScript)
- Dynamic task table  
- Add, edit, delete tasks  
- Fully handled via **Fetch API**  
- Zero server-side data passing in templates  

### 🔹 Engineering Highlights
- SQLite database powered by **raw SQL service layer**  
- Separation of **API Views** and **Template Views**  
- Centralized `TaskService` for all DB operations  
- Minimal, maintainable template structure  
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

Access the application:

👉 http://127.0.0.1:8000/

### 🔑 Admin Panel Access
If you want to view or verify the **existing sample data** that I included during development, you may log in using:

```
URL: http://127.0.0.1:8000/admin/
Username: admin
Password: admin
```

(Note: This admin account exists only because SQLite and DB data were pushed for assignment demonstration.)

---

# 🖥 Run Locally (Without Docker)

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 3️⃣ Apply Migrations

```bash
python manage.py migrate
```

## 4️⃣ Start the Django Development Server

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

### ✔ Get Single Task
```http
GET /api/detail/<id>/
```

### ✔ Create a New Task
```http
POST /api/create/
```

#### Example Request
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
