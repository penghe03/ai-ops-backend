# AI Ops Backend (FastAPI)

An AI-assisted incident management backend built with FastAPI and SQLAlchemy.
🚀 Built by a Software Engineer II focusing on backend systems and AI integration

## 🚀 Features

* RESTful API for issue tracking
* Create, list, and update issues
* Severity-based filtering
* Status workflow (open → in-progress → resolved)
* AI-generated suggested fixes (mock)
* Input validation with Pydantic

## 🛠 Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic

## 📦 Project Structure

```
app/
├── main.py
├── db/
│   ├── models.py
│   └── session.py
├── routers/
│   └── issues.py
├── services/
│   ├── ai.py
│   └── issue_service.py
└── schemas/
    └── issue.py
```

## ▶️ How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Start server:

```
uvicorn app.main:app --reload
```

3. Open API docs (to be updated):

```
http://127.0.0.1:8000/docs
```

## 🐳 Run with Docker

```bash
docker build -t ai-ops-backend .
docker run -p 8000:8000 ai-ops-backend


## 📌 Example API Usage

### Create an Issue

POST /issues

```
{
  "title": "Login failure",
  "description": "Users cannot log in",
  "severity": "high"
}
```

### Response

```
{
  "title": "Login failure",
  "description": "Users cannot log in",
  "severity": "high",
  "status": "open",
  "suggested_fix": "Investigate 'Login failure'. Check logs and related services."
}
```

## 📈 Future Improvements

* Integrate real LLM API for suggestions
* Add authentication (JWT)
* Add pagination and sorting
* Deploy to cloud (AWS / GCP)

## 🌍 Live Demo

https://ai-ops-backend.onrender.com/docs

## 👤 Author

Built as part of backend engineering practice and interview preparation.

