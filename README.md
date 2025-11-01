# ✅ Django To-Do List App  

A clean and functional **To-Do web application** built using **Django**.  
Users can register, log in, and manage their personal task lists — add, edit, mark complete, or delete tasks.  
This project focuses on **CRUD functionality** (Create, Read, Update, Delete) and Django authentication.

---

## 🚀 Features

### 👤 User Features
- Register and Login using Django’s built-in authentication
- Add new tasks with title and description
- Edit and update existing tasks
- Mark tasks as completed / uncompleted
- Delete tasks
- Fully private task lists — every user sees only their own tasks

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-------------|
| Backend | **Django** |
| Frontend | HTML, CSS, JavaScript (basic) |
| Database | SQLite |
| Authentication | Django’s session-based auth |
| IDE | VS Code / PyCharm |

---

## ⚙️ Installation Guide

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/django-todo-app.git
cd django-todo-app

2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # For Windows
source venv/bin/activate   # For macOS/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Apply migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create a superuser (optional)
python manage.py createsuperuser

6️⃣ Run the server
python manage.py runserver


Visit:
👉 http://127.0.0.1:8000/

![Login Page](screenshots/login.png)
<img width="656" height="609" alt="image" src="https://github.com/user-attachments/assets/94e067a9-94d8-44f4-8f81-d3b8bac73d09" />

![Dashboard](screenshots/dashboard.png)

<img width="1328" height="727" alt="image" src="https://github.com/user-attachments/assets/b6fe4eb8-518d-475e-aa52-9f210d2b2812" />


git clone https://github.com/yourusername/django-todo-app.git
cd django-todo-app
