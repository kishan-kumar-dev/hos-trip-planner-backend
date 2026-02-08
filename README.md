
```markdown
# Backend — HOS Trip Planner (Django)

This repository contains the backend service for the **Hours of Service (HOS) Trip Planner** application.

The backend exposes a REST API that calculates:
- driving hours
- rest hours
- total trip hours
- cycle usage

The logic is intentionally simplified to demonstrate backend design and API correctness for an assessment.

---

## 🛠 Tech Stack

- **Python 3.x**
- **Django**
- **Django REST Framework**
- **SQLite** (local development)
- **django-cors-headers**

---

## 📁 Project Structure

```

backend/
└── server/
├── server/
│   ├── **init**.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── trips/
│   ├── **init**.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
└── db.sqlite3

````

---

## 🚀 Setup Instructions (Local)

### 1️⃣ Create virtual environment

```bash
python -m venv venv
````

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

---

### 2️⃣ Install dependencies

```bash
pip install django djangorestframework django-cors-headers
```

---

### 3️⃣ Run migrations

```bash
cd backend/server
python manage.py migrate
```

---

### 4️⃣ Start development server

```bash
python manage.py runserver
```

Backend will be available at:

```
http://127.0.0.1:8000
```

---

## 🔗 API Endpoint

### **POST** `/api/calculate/`

#### Request Body (JSON)

```json
{
  "current": "New York",
  "pickup": "Chicago",
  "dropoff": "Los Angeles",
  "miles": 1200,
  "cycle_used": 12
}
```

#### Response (JSON)

```json
{
  "current": "New York",
  "pickup": "Chicago",
  "dropoff": "Los Angeles",
  "miles": 1200.0,
  "driving_hours": 20.0,
  "rest_hours": 1,
  "total_hours": 21.0,
  "cycle_used": 12.0
}
```

---

## 🧠 Business Logic (Simplified)

* Driving speed is assumed to be **60 miles/hour**
* Driving hours = `miles / 60`
* A fixed **1 hour rest** is added
* Total hours = driving hours + rest hours
* Cycle usage is accepted as input and returned
* Logic is simplified for assessment/demo purposes only

---

## 🌐 CORS Configuration

CORS is enabled to allow requests from a frontend application such as React:

```
http://localhost:3000
```

---

## 📌 Notes

* Designed for **coding assessment / demonstration**
* No authentication required
* SQLite used for simplicity
* Focus is on clean API design and correctness

---

## 👤 Author

**Kishan Kumar**
Full Stack Developer Candidate
Spotter AI Coding Assessment

```