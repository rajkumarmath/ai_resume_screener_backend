from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class JobCreate(BaseModel):
    title: str
    description: str
    skills: Optional[List[str]] = []  # ✅ Make skills a list

class JobResponse(BaseModel):
    id: int
    title: str
    description: str
    skills: List[str]
    created_at: datetime

    class Config:
        orm_mode = True

