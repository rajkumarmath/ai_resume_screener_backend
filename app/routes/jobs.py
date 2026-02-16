from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.explainer import generate_explanation
from app.models.job import Job
from app.models.resume import Resume
from app.schemas.job import JobCreate, JobResponse
from app.services.openai_matcher import get_embedding, cosine_similarity

router = APIRouter()


@router.post("/", response_model=JobResponse)
def create_job(job: JobCreate, db: Session = Depends(get_db)):

    job_text = f"""
	Title: {job.title}
	Skills Required: {', '.join(job.skills or [])}
	Job Description:
	{job.description}
	"""


    embedding = get_embedding(job_text)

    db_job = Job(
        title=job.title,
        skills=job.skills,
        description=job.description,
        embedding=embedding
    )

    db.add(db_job)
    db.commit()
    db.refresh(db_job)

    return db_job
@router.get("/{job_id}/match")
def match_resumes(job_id: int, db: Session = Depends(get_db)):

    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    if not job.embedding:
        raise HTTPException(status_code=400, detail="Job has no embedding")

    resumes = db.query(Resume).all()

    results = []

    for r in resumes:
        if not r.embedding:
            continue

        score = cosine_similarity(job.embedding, r.embedding)

        results.append({
            "id": r.id,
            "user_id": r.user_id,
            "name": r.name,
            "skills": r.skills,
            "score": round(score, 4)
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results

@router.get("/{job_id}/match-with-explanation")
def match_resumes_with_explanation(job_id: int, db: Session = Depends(get_db)):

    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    resumes = db.query(Resume).all()

    results = []

    for resume in resumes:
        score = cosine_similarity(job.embedding, resume.embedding)

        explanation = generate_explanation(
            job.description,
            resume.content,
            score
        )

        results.append({
            "resume_id": resume.id,
            "score": score,
            "explanation": explanation
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results

