# 🧠 Dev Tracker

A full-stack DSA (Data Structures & Algorithms) practice tracker built with **FastAPI** and **Streamlit**. Designed with a production-grade layered architecture — log problems daily, track consistency through a streak calendar, and visualize progress through charts.

---

## 🚀 Features

- 🔐 JWT authentication with bcrypt password hashing
- ✅ Email format validation + strong password enforcement on registration
- 📝 Log DSA problems with topic, difficulty, and date
- 📅 LeetCode-style monthly streak calendar
- 🔥 Automatic streak counter (cross-month aware)
- 📊 Pie charts by difficulty and topic
- 📋 Paginated tabular view of solved problems
- 👤 Per-user data isolation — each user only sees their own data
- 🏗️ Clean service/repository architecture with full separation of concerns

---

## 🛠️ Tech Stack

| Layer        | Technology                    |
| ------------ | ----------------------------- |
| Backend      | FastAPI                       |
| Frontend     | Streamlit                     |
| Database     | SQLAlchemy ORM + SQLite (dev) |
| Auth         | JWT (python-jose) + bcrypt    |
| Validation   | Pydantic + email-validator    |
| Charts       | Matplotlib                    |
| Data Display | Pandas                        |

---

## 🏗️ Architecture

This project follows a **3-layer architecture** to separate concerns cleanly:

```
HTTP Request
     ↓
  Routers         → handles HTTP, input/output only
     ↓
  Services        → business logic, validation, error handling
     ↓
 Repositories     → database queries only, no business logic
     ↓
  SQLAlchemy ORM  → talks to the database
```

This makes the codebase easy to extend — swapping SQLite for PostgreSQL, for example, only requires a one-line change in `database.py`.

---

## 📁 Project Structure

```
fastapi/
│
├── main.py                  # FastAPI app, lifespan, and route registration
├── database.py              # SQLAlchemy engine, SessionLocal, Base
├── models.py                # Pydantic request/response models
├── models_db.py             # SQLAlchemy ORM table definitions
├── auth_utils.py            # JWT token creation and verification
├── utils.py                 # Streak calculator, email/password validators
├── frontend.py              # Login page (Streamlit)
│
├── routers/
│   └── auth.py              # /register, /login routes
│
├── services/
│   ├── user_service.py      # User business logic + HTTP error handling
│   └── problem_service.py   # Problem business logic
│
├── repository/
│   ├── user_repository.py   # User DB queries
│   └── problem_repository.py# Problem DB queries
│
└── pages/
    ├── register.py          # Registration page (Streamlit)
    └── tracker.py           # Main tracker dashboard (Streamlit)
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/YashAgarwalTheWiz/Fast_API_Dev_Tracker.git
cd Fast_API_Dev_Tracker/fastapi
```

### 2. Create a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn streamlit requests python-jose passlib bcrypt==4.0.1 matplotlib pandas sqlalchemy psycopg2-binary email-validator
```

### 4. Run the backend

```bash
uvicorn main:app --reload
```

Tables are created automatically on startup via FastAPI lifespan events — no manual setup needed.

### 5. Run the frontend

```bash
streamlit run frontend.py
```

---

## 📌 Usage

1. Register a new account (email validated, strong password enforced)
2. Login with your credentials
3. Log a DSA problem — enter problem name, topic, and difficulty
4. View your monthly streak calendar — activity shown as ✅
5. Check progress via pie charts (by difficulty and topic)
6. Browse paginated problem history (`?page=1&limit=20`)

---

## 🔌 API Endpoints

| Method | Endpoint                | Auth | Description                         |
| ------ | ----------------------- | ---- | ----------------------------------- |
| POST   | `/register`             | ❌   | Register a new user                 |
| POST   | `/login`                | ❌   | Login and receive JWT token         |
| POST   | `/insert_data`          | ✅   | Log a new DSA problem               |
| GET    | `/my_problems`          | ✅   | Get paginated problem list          |
| GET    | `/activedates`          | ✅   | Get all active dates (for streak)   |
| GET    | `/count_by_difficulty`  | ✅   | Problem count grouped by difficulty |
| GET    | `/count_by_topic`       | ✅   | Problem count grouped by topic      |
| GET    | `/filter_by_difficulty` | ✅   | Filter problems by difficulty       |

Interactive API docs available at `http://127.0.0.1:8000/docs`

---

## 👨‍💻 Author

**Yash Agarwal**
[GitHub](https://github.com/YashAgarwalTheWiz)
