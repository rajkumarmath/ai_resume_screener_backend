from pydantic import BaseModel
from typing import List, Optional

class ResumeCreate(BaseModel):
    file_path: str
    parsed_text: Optional[str] = None
    skills: Optional[List[str]] = None  # ✅ Add skills here too

class ResumeResponse(BaseModel):
    id: int
    file_path: str
    parsed_text: Optional[str]
    uploaded_at: str
    skills: List[str]

    class Config:
        orm_mode = True

class ResumeOut(BaseModel):
    id: int
    user_id: int
    name: str
    skills: List[str]  # ✅ Always as list

    class Config:
        orm_mode = True

