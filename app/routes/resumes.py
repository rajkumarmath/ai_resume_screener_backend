
from app.services.openai_matcher import get_embedding
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.resume import Resume
import PyPDF2
import io

router = APIRouter(tags=["Resumes"])


def extract_text_from_pdf(file_bytes: bytes):
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text() or ""

    return text


@router.post("/upload")
async def upload_resume(
    user_id: int,
    name: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    # Read PDF
    file_bytes = await file.read()

    # Extract text
    resume_text = extract_text_from_pdf(file_bytes)

    if not resume_text.strip():
        return {"error": "Could not extract text from PDF"}

    # Generate embedding using Gemini
    embedding = get_embedding(resume_text)

    # Save to DB
    db_resume = Resume(
        user_id=user_id,
        name=name,
        content=resume_text,
        skills=[],  # optional for now
        embedding=embedding
    )

    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)

    return {
        "message": "Resume uploaded successfully",
        "resume_id": db_resume.id
    }
