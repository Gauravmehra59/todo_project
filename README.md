# 📝 To-Do List Project (Django + REST API + Templates)

A fully functional **To-Do List Web Application** built using **Django**.

This project includes:

- Full CRUD **REST APIs**
- Clean **Template-based UI**
- SQLite database
- Professional folder structure
- Easy to run & deploy

---

## 🚀 Features

### 🔹 API Features
- Create task  
- Read task  
- Update task  
- Delete task (**204 No Content**)  
- JSON REST API responses  

### 🔹 UI Features
- Add / Edit / Delete tasks  
- Simple HTML templates  

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository
```
git clone git@github.com:Gauravmehra59/todo_project.git
cd todo_project
```

### 3️⃣ Install Requirements
```
pip install -r requirements.txt
```

### 4️⃣ Run Migrations
```
python manage.py migrate
```

### 5️⃣ Start Server
```
python manage.py runserver
```

Open your browser:

http://127.0.0.1:8000/  

---

## 📮 API Endpoints

### ✔ Get All Tasks
```
GET /api/list/
```

### ✔ Get Single Task
```
GET /api/detail/<id>/
```

### ✔ Create Task
```
POST /api/create/
```

#### Example Body:
```json
{
  "title": "Buy Eggs",
  "description": "6 eggs",
  "due_date": "2025-11-21",
  "status": "pending"
}
```

### ✔ Update Task
```
PUT /api/update/<id>/
```

### ✔ Delete Task
```
DELETE /api/delete/<id>/
```

---

## Run Test Cases
```
pytest -v
```

---
## 🛠 Tech Stack

- Python 3+
- Django
- HTML / CSS / JS
- SQLite (default)
