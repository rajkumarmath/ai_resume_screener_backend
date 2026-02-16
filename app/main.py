from fastapi import FastAPI, Depends
from app.routes import users, resumes, jobs
from app.database import Base, engine
from app.database import get_db
from sqlalchemy import text
from app.models.job import Job
from app.models.resume import Resume
from app.models.user import User

app = FastAPI(title="AI Resume System", version="1.0")
Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(resumes.router, prefix="/resumes", tags=["Resumes"])
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])

@app.get("/", tags=["Default"])
def health_check():
    return {"status": "ok"}

@app.get("/debug-db")
def debug_db(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT current_database();"))
    return {"database": result.scalar()}

@app.get("/debug-columns")
def debug_columns(db: Session = Depends(get_db)):
    result = db.execute(text("""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = 'jobs'
        AND table_schema = 'public';
    """))
    return {"columns": [row[0] for row in result]}
@app.get("/debug-user")
def debug_user(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT current_user;"))
    return {"user": result.scalar()}

