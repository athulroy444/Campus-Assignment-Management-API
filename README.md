# Campus Assignment Management API

This is a REST API for a College Assignment Management System built with Django REST Framework and MySQL.

## Features
- **Student Authentication**: Register and Login using JWT.
- **Assignment Management**: CRUD operations for student assignments.
- **Ownership Protection**: Students can only access and manage their own assignments.

## Tech Stack
- **Framework**: Django 5.1
- **API Engine**: Django REST Framework (DRF)
- **Authentication**: SimpleJWT
- **Database**: MySQL

## Setup Instructions

### 1. Prerequisites
- Python 3.10+
- MySQL Server

### 2. Database Configuration
Create a database named `campus_api` in your MySQL server:
```sql
CREATE DATABASE campus_api;
```

Update the database credentials in `campus_project/settings.py` if necessary:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'campus_api',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### 3. Installation
1. Clone the repository and navigate to the project directory.
2. Install dependencies:
   ```bash
   pip install django djangorestframework djangorestframework-simplejwt mysqlclient
   ```

### 4. Migrations
Run the following commands to set up the database schema:
```bash
python manage.py makemigrations api
python manage.py migrate
```

### 5. Run Server
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- `POST /api/register/`: Register a new student.
- `POST /api/login/`: Login and get JWT tokens (access & refresh).

### Assignments (Authenticated)
- `GET /api/assignments/`: List all assignments for the logged-in student.
- `POST /api/assignments/`: Create a new assignment.
- `GET /api/assignments/{id}/`: View a specific assignment.
- `PUT /api/assignments/{id}/`: Update an assignment.
- `DELETE /api/assignments/{id}/`: Delete an assignment.

## Sample Request (Registration)
```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "password123",
    "department": "Computer Science",
    "year": 3
}
```

## Postman Collection
A Postman collection named `Campus_Assignment_Management_API.postman_collection.json` is included in the root directory.
