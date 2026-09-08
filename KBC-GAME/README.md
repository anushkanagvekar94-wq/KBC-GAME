# KBC Game

## Stack
React + Tailwind CSS + FastAPI + MySQL.

## 1. MySQL
Create the database:
```sql
CREATE DATABASE kbc_game;
```

## 2. Backend
```bash
cd backend
python -m venv venv
# Windows:
venv\Scripts\activate
pip install -r requirements.txt
```
Copy `.env.example` to `.env` and set your MySQL password.

Start API:
```bash
uvicorn app.main:app --reload
```

In another terminal, seed questions:
```bash
python seed.py
```

API: http://localhost:8000
Swagger: http://localhost:8000/docs

## 3. Frontend
```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173

## Admin
Register/login using `admin@kbc.com` to access the admin endpoint. For a real application, replace this demo email check with a proper role field and authorization system.

## Important
This is a complete educational starter project. Before production, add stronger validation, refresh tokens, rate limiting, secure secrets, proper admin roles, question randomization, server-side game state validation, and HTTPS.
