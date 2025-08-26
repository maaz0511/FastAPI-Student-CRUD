# 📚 Student CRUD API with FastAPI

A simple yet powerful **CRUD API** built using **FastAPI** to manage student records.
This project demonstrates how to create, read, update, and delete student details stored in a JSON file — keeping things minimal, clean, and easy to understand 🚀.

---

## ✨ Features

* 📝 **Create** new student records
* 📖 **Read** all students or a specific student by ID
* ✏️ **Update** existing student details
* 🗑️ **Delete** a student record
* 📊 Stores data in `data.json` for simplicity
* ⚡ Powered by **FastAPI + Pydantic + Uvicorn**

---

## 📂 Project Structure

```
.
├── main.py           # FastAPI routes for CRUD operations
├── logic.py          # Functions to load & save JSON data
├── schemas.py        # Pydantic models for validation
├── data.json         # Student records (acts as a database)
├── requirements.txt  # Dependencies
└── Procfile          # Deployment config (Render/Heroku)
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repo

```bash
git clone https://github.com/maaz0511/FastAPI-Student-CRUD.git
cd fastapi-student-crud
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app

```bash
uvicorn main:app --reload
```

👉 The API will be live at:
`http://127.0.0.1:8000`

---

## 🌐 API Endpoints

| Method | Endpoint         | Description                     |
| ------ | ---------------- | ------------------------------- |
| GET    | `/`              | Welcome message                 |
| GET    | `/students`      | Get all students (sorted by ID) |
| GET    | `/students/{id}` | Get a single student by ID      |
| POST   | `/students`      | Add a new student               |
| PUT    | `/students/{id}` | Update a student by ID          |
| DELETE | `/students/{id}` | Delete a student by ID          |

---

## 📖 API Docs

FastAPI provides interactive docs automatically 🎉

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🚀 Deployment on Render

This project is **Render-ready**.

* The `Procfile` ensures Render knows how to start the app:

  ```bash
  web: uvicorn main:app --host 0.0.0.0 --port $PORT
  ```
* Just connect your GitHub repo to Render → create a **Web Service** → and you’re live! 🌍

---

## 📊 Sample Data (`data.json`)

```json
[
  {
    "id": 1,
    "name": "Poonam Sharma",
    "age": 12,
    "roll_num": 21,
    "std_class": 6,
    "marks": {
      "english": 78,
      "hindi": 82,
      "maths": 91,
      "computer": 88
    },
    "contact": 9876543210
  },
  {
    "id": 2,
    "name": "Priya Verma",
    "age": 13,
    "roll_num": 18,
    "std_class": 7,
    "marks": {
      "english": 85,
      "hindi": 79,
      "maths": 88,
      "computer": 92
    },
    "contact": 9876501234
  }
]
```

---

## 💡 Why This Project?

I built this project to **learn and demonstrate**:

* FastAPI fundamentals
* JSON-based storage as a mini-database
* CRUD API design
* Deployment workflow on Render

---

✨ Created by Mohd Maaz
