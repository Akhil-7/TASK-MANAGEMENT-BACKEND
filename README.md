# TaskManagement

A Django-based backend application for managing tasks and users. This project is structured into multiple apps for better modularity.

## 📁 Project Structure

```
TaskManagement/
├── API/                      # Aggregator app for routing
│   ├── urls.py              # API-level routing
│
├── taskManage/              # App for managing tasks
│   ├── admin.py
│   ├── apps.py
│   ├── models.py            # Task model definition
│   ├── serializers.py       # Serializers for task models
│   ├── tests.py
│   ├── urls.py              # App-specific routes
│   ├── views.py             # Task-related views
│
├── taskManagement/          # Project settings
│   ├── settings.py
│   ├── urls.py              # Root URL configuration
│   ├── asgi.py
│   ├── wsgi.py
│
├── userManage/              # App for managing users
│   ├── admin.py
│   ├── apps.py
│   ├── models.py            # User model definition
│   ├── serializers.py       # Serializers for user models
│   ├── tests.py
│   ├── urls.py              # App-specific routes
│   ├── views.py             # User-related views
│
├── db.sqlite3               # SQLite database
├── manage.py                # Django CLI utility
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Django 3.2+
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/taskmanagement.git
   cd taskmanagement
   ```

2. **Create and activate a virtual environment**  
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**  
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**  
   ```bash
   python manage.py runserver
   ```

6. **Access the API**  
   Navigate to `http://127.0.0.1:8000/` in your browser or use tools like Postman.



## 📦 API Overview

The APIs are split into two major parts:

- **Task Management**: Create, update, delete, and retrieve tasks.
- **User Management**: Register, authenticate, and manage users.

## 🔧 Configuration

All project-level settings can be found in:

```
taskManagement/settings.py
```

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 📌 API Endpoints

### 🔐 User Management (`/account/`)
| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| POST   | `/register/`     | Register a new user      |
| POST   | `/login/`        | Authenticate a user      |

### ✅ Task Management (`/task/`)
| Method | Endpoint             | Description                      |
|--------|----------------------|----------------------------------|
| GET    | `/tasks/`            | Retrieve all tasks               |
| POST   | `/tasks/`            | Create a new task                |
| GET    | `/tasks/<int:pk>/`   | Retrieve a specific task         |
| PUT    | `/tasks/<int:pk>/`   | Update a specific task           |
| DELETE | `/tasks/<int:pk>/`   | Delete a specific task           |
| GET    | `/home/`             | View dashboard summary or stats  |