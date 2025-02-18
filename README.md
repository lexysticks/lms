# Mini LMS Backend

This project is a **Mini Learning Management System (LMS) Backend** built with **Django REST Framework (DRF)**. It provides a REST API for managing courses and enrollments.

## Features

### 1. Course Management

- **Create a Course:** `POST /courses/`
- **List All Courses:** `GET /courses/`
- **Get Course by ID:** `GET /courses/{id}/`
- **Update Course:** `PUT /courses/{id}/`
- **Delete Course:** `DELETE /courses/{id}/`

### 2. Enrollment Management

- **Enroll a User:** `POST /enrollments/`
- **List All Enrollments:** `GET /enrollments/`

## Technical Stack

- **Django REST Framework** for API development.
- **SQLite** as the database.
- **Token-based authentication** for protected routes.
- **Foreign key relationships** between Courses and Enrollments.

## Installation and Setup

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/mini-lms-backend.git
cd mini-lms-backend
```

### 2. Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\\Scripts\\activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Run Database Migrations

```sh
python manage.py migrate
```

### 5. Create a Superuser (Optional)

```sh
python manage.py createsuperuser
```

### 6. Start the Development Server

```sh
python manage.py runserver
```

## Authentication

- The API uses **Token-based authentication**.
- Obtain a token by sending a **POST** request to `/api/token/` with your login credentials.

## Example API Requests

### 1. Get All Courses

```sh
curl -X GET https://lms-9r15.onrender.com/courses/
```

### 2. Create a Course (Authenticated)

```sh
curl -X POST https://lms-9r15.onrender.com/courses/ \\
     -H "Authorization: Token your_token_here" \\
     -H "Content-Type: application/json" \\
     -d '{"title": "Django Basics", "description": "Learn Django", "price": 20}'
```

### 3. Enroll a User in a Course

```sh
curl -X POST https://lms-9r15.onrender.com/enrollments/ \\
     -H "Authorization: Token your_token_here" \\
     -H "Content-Type: application/json" \\
     -d '{"user_id": 1, "course_id": 2}'
```

## Deployment

The project is deployed on **Render**.

- **Live API URL:** [https://lms-9r15.onrender.com/]
- **Test Account:**
  - **Email:** testuser@gmail.com
  - **Password:** testpassword

## Contributing

Feel free to submit issues or create pull requests.

## License

This project is licensed under the **MIT License**.
