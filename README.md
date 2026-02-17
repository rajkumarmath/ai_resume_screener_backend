# 🚀 AI Resume screener Matching Backend

A production-ready FastAPI backend for an AI-powered Job Matching platform.
**🔗 Live Demo:** [View Here](https://ai-resume-screener-gr9g.onrender.com)
** To test endpoints:** [check docs](https://ai-resume-screener-gr9g.onrender.com/docs)
# 📌 What This Project Does

This backend powers an AI-driven Job–Resume Matching System.

It allows:

* Recruiters to post jobs
* Jobs to be converted into AI embeddings using Google Gemini
* Resume embeddings to be compared semantically
* Intelligent similarity scoring between jobs and resumes
* AI-generated explanation for match quality

Instead of keyword matching, this system performs **semantic vector similarity matching**, meaning it understands context — not just exact words.

---

# ❗ The Problem

Traditional job portals rely on:

* Keyword matching
* Basic filters
* Manual screening

This creates several issues:

1. **Keyword dependency problem**
   If a resume says “REST API development” but the job says “Backend API design”, traditional systems may fail to match them.

2. **High recruiter workload**
   Recruiters manually review hundreds of resumes.

3. **Lack of explainability**
   Most AI systems return a score but do not explain *why* the match occurred.

4. **Surface-level matching**
   Matching is based on text overlap, not semantic understanding.

---

# 💡 Our Solution

This backend solves the above problems using:

### 1️⃣ AI Embeddings (Gemini)

When a job is created:

* The description + skills are sent to Gemini
* A high-dimensional embedding vector is generated
* Stored in PostgreSQL

Embeddings capture semantic meaning, not just keywords.

---

### 2️⃣ Vector Similarity Matching

When matching resumes to jobs:

* Resume embeddings are compared with job embeddings
* Cosine similarity is calculated
* Results are ranked by similarity score

This allows:

* Context-aware matching
* Skill similarity recognition
* Better ranking quality

---

### 3️⃣ AI-Powered Explanation

The system uses Gemini again to generate:

* Human-readable explanation of why a resume matches a job

Example:

> "This resume matches the required Python backend experience and REST API development skills."

This improves:

* Recruiter trust
* Transparency
* Decision speed

---

# 🧠 Why This Is Better Than Keyword Matching

| Traditional Matching   | This System                 |
| ---------------------- | --------------------------- |
| Exact keyword required | Understands context         |
| Misses synonyms        | Detects semantic similarity |
| Manual review heavy    | Ranked scoring              |
| No explanation         | AI-generated reasoning      |

---

# 🏗 Architecture Overview

Flow:

1. Job is submitted
2. Backend calls Gemini → embedding generated
3. Embedding stored in PostgreSQL
4. Resume embeddings compared using cosine similarity
5. Matches ranked
6. Explanation generated via Gemini

Tech stack:

* FastAPI
* PostgreSQL
* SQLAlchemy
* Gemini Pro API
* Vector similarity using NumPy

---

# 🎯 Real-World Use Case

* HR tech startups
* Internal hiring systems
* Resume screening automation
* AI-assisted recruitment tools

---

# 🚀 Why This Project Matters

This is not a CRUD demo.

It demonstrates:

* AI API integration
* Vector embeddings
* Semantic similarity
* Clean backend architecture
* Production deployment on Render
* Database schema handling
* Real-world problem solving

This is backend + AI engineering combined.


This backend allows:
- Recruiters to upload jobs
- Jobs to be stored with vector embeddings
- Users to retrieve job listings
- Semantic search (AI-powered matching)

Built with FastAPI, PostgreSQL, SQLAlchemy, and Gemini embeddings.

---

## 🧱 Tech Stack

- **FastAPI** – Web framework
- **PostgreSQL** – Database (Render)
- **SQLAlchemy** – ORM
- **Pydantic** – Data validation
- **Google Gemini Pro** – Text embeddings
- **Uvicorn** – ASGI server
- **Render** – Deployment

---

## 📂 Project Structure
backend/
│
├── app/
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── database.py
│ ├── crud.py
│ ├── routes/
│ │ └── jobs.py
│
├── requirements.txt
└── README.md

---

## ⚙️ Environment Variables

Create a `.env` file:
DATABASE_URL=postgresql://user:password@host:port/dbname
GEMINI_API_KEY=your_gemini_api_key


If deploying on Render, add these in the **Environment tab**.

---

## 🗄 Database Schema

### Jobs Table

| Column       | Type      | Description |
|--------------|-----------|-------------|
| id           | Integer   | Primary Key |
| title        | String    | Job title |
| description  | Text      | Job description |
| skills       | JSON      | Required skills |
| embedding    | JSON      | Gemini vector embedding |
| created_at   | Timestamp | Default NOW() |

---

## 🔥 API Endpoints

### 1️⃣ Create Job

**POST** `/jobs/`
Request:

```json
{
  "title": "AI Developer",
  "description": "Build AI systems",
  "skills": ["python", "machine learning"]
}
Response:

{
  "id": 1,
  "title": "AI Developer",
  "description": "Build AI systems",
  "skills": ["python", "machine learning"],
  "created_at": "2026-02-17T13:32:32"
}


2️⃣ Get All Jobs

GET /jobs/

Response:

[
  {
    "id": 1,
    "title": "AI Developer",
    "description": "Build AI systems",
    "skills": ["python", "machine learning"],
    "created_at": "2026-02-17T13:32:32"
  }
]

🧠 Embedding Flow

Job is submitted
Gemini API generates embedding
Embedding stored as JSON vector
Used for semantic similarity search

▶️ Running Locally
1. Clone Repository
git clone https://github.com/rajkumarmath/ai_resume_screener_backend.git
cd backend
2. Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
3. Install Dependencies
pip install -r requirements.txt
4. Run Server
uvicorn app.main:app --reload

Visit:
http://127.0.0.1:8000/docs
Swagger UI will appear.


🧪 Testing Endpoints
Use:
Swagger UI
Postman
Thunder Client (VS Code)

🚀 Deployment (Render)
Push code to GitHub
Create new Web Service in Render
Connect repo
Add environment variables
Deploy

🛑 Common Errors
column created_at does not exist
Fix:
ALTER TABLE jobs
ADD COLUMN created_at TIMESTAMP DEFAULT NOW();

🔐 Security Notes
Never commit .env
Use strong database credentials
Restrict CORS properly in production

📌 Future Improvements
Authentication (JWT)
Role-based access
Vector similarity search in DB
Pagination
Filtering by skills
CI/CD pipeline
Alembic migrations
```
👨‍💻 Author

Built by Rajkumar

