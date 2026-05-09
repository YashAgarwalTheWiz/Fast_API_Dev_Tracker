# 🧠 Dev Tracker

A personal DSA (Data Structures & Algorithms) practice tracker built with FastAPI and Streamlit. Log the problems you solve daily, track your consistency through a streak calendar, and visualize your progress through charts.

## 🚀 Features

- 🔐 User authentication with JWT tokens and bcrypt password hashing
- 📝 Log DSA problems with topic, difficulty, and date
- 📅 LeetCode-style monthly streak calendar — green boxes for active days
- 🔥 Automatic streak counter
- 📊 Pie charts by difficulty and topic
- 📋 Tabular view of all your solved problems
- 👤 Each user sees only their own data

## 🛠️ Tech Stack

| Layer        | Technology                 |
| ------------ | -------------------------- |
| Backend      | FastAPI                    |
| Frontend     | Streamlit                  |
| Database     | SQLite                     |
| Auth         | JWT (python-jose) + bcrypt |
| Charts       | Matplotlib                 |
| Data Display | Pandas                     |

## 📁 Project Structure

```
fastapi/
│
├── main.py              # FastAPI app and routes
├── models.py            # Pydantic models
├── dao.py               # Database access layer
├── auth_utils.py        # JWT token logic
├── frontend.py          # Login page
│
├── pages/
│   ├── register.py      # Registration page
│   └── tracker.py       # Main tracker page
│
├── routers/
│   └── auth.py          # Auth routes
│
└── utils.py             # Streak calculation logic
```

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/YashAgarwalTheWiz/Fast_API_Dev_Tracker.git
cd Fast_API_Dev_Tracker
```

### 2. Create a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn streamlit requests python-jose passlib matplotlib pandas
```

### 4. Run the backend

```bash
uvicorn main:app --reload
```

### 5. Run the frontend

```bash
streamlit run frontend.py
```

## 📌 Usage

1. Register a new account
2. Login with your credentials
3. Log a DSA problem — enter problem name, topic, and difficulty
4. View your monthly streak calendar
5. Check your progress via pie charts and data table

## 👨‍💻 Author

**Yash Agarwal**  
[GitHub](https://github.com/YashAgarwalTheWiz)

```

```
