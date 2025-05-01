# B2B Marketplace - Backend

This is the backend of the mini B2B marketplace built using **FastAPI + PostgreSQL**.

## 🚀 Features

- Manufacturer listing API
- Search and filter by name/city/category
- Pagination support
- Manufacturer detail API
- Admin endpoints (Add/Edit/Delete)
- Dummy login with JWT token
- CORS enabled for frontend access

---

## 🛠️ Tech Stack

- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn
- Pydantic
- JWT (via `python-jose`)

---

## 📦 Installation

cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
▶️ Run Locally
uvicorn app.main:app --reload
Access: http://localhost:8000/docs

🌐 Environment Variables
Make sure database.py has a connection like:
SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@localhost:5432/b2b_marketplace"

🔐 Dummy Login
POST /auth/login

username: admin
password: admin123
Returns JWT token. Use this in Authorization: Bearer <token> for protected endpoints.

📥 Seed Sample Data
Run this once:
python app/seed.py

✅ API Endpoints
GET /manufacturers

GET /manufacturers/{id}

POST /manufacturers

PUT /manufacturers/{id}

DELETE /manufacturers/{id}

POST /auth/login
