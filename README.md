# Backend Developer Internship Assignment

## Project Overview

This project implements a scalable REST API with authentication and CRUD functionality.  
Users can register, login, and manage notes through secure APIs.  
A simple frontend UI is also included to interact with the backend.

---

## Tech Stack

Backend:
- Python
- FastAPI
- SQLAlchemy
- JWT Authentication

Database:
- SQLite

Frontend:
- HTML
- JavaScript

Tools:
- Git
- GitHub
- Swagger API Documentation

---

## Features

User Authentication
- User registration
- User login
- Password hashing
- JWT token generation

CRUD Operations
- Create notes
- View notes
- Delete notes

API Documentation
- Swagger UI for testing APIs

---

## Project Structure

backend-intern-assignment

backend
- main.py
- database.py
- models.py
- schemas.py
- auth.py
- notes.py

frontend
- index.html
- script.js

requirements.txt
README.md

---

## Installation

Clone the repository

git clone <your-repo-link>

Navigate to project folder

cd backend-intern-assignment

Install dependencies

pip install -r requirements.txt

Run the backend server

cd backend

python -m uvicorn main:app --reload

---

## API Documentation

After running the server, open:

http://127.0.0.1:8000/docs

This provides interactive API testing using Swagger UI.

---

## Scalability Approach

The backend is designed with a modular structure to support scalability.

Future improvements may include:
- Redis caching
- Docker containerization
- Microservices architecture
- Load balancing

---

## Author

Divya Kotlo