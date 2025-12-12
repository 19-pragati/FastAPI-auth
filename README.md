# FastAPI Auth API – Simple Signup & Login System

This is a beginner-friendly FastAPI authentication API that includes user signup and login functionality using:

- Password hashing (bcrypt via Passlib)
- FastAPI framework
- Interactive API testing using Swagger UI
- Pydantic models for validation
- Uvicorn ASGI server

This project demonstrates API development, authentication basics, and secure password handling.

---

## Features

### Signup (POST /signup)
- Accepts `username` and `password`
- Hashes password using bcrypt
- Stores user in in-memory dictionary
- Returns a success message

### Login (POST /login)
- Verifies that the user exists
- Validates password against hashed value
- Returns a success or error message

### Additional Features
- Auto-generated API documentation at `/docs`
- Clean and simple code structure
- Can be extended with a real database and JWT authentication

---
## Project Structure

---

## How to Run the Project

### 1. Create a virtual environment

### 2. Activate the environment (Windows)

### 3. Install the required packages

### 4. Start the FastAPI server

### 5. Open API documentation

---

## Example JSON Input

### Signup
```json
{
  "username": "pragati",
  "password": "123"
}

Technologies Used

Python

FastAPI

Uvicorn

Passlib (for password hashing)

Pydantic

Future Improvements

This project can be expanded with:

JWT-based authentication

Database integration instead of in-memory storage

Password reset flow

Docker support for deployment

