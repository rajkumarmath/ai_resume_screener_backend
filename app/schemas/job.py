from pydantic import BaseModel
from typing import List, Optional

class JobCreate(BaseModel):
    title: str
    description: str
    skills: Optional[List[str]] = []  # ✅ Make skills a list

class JobResponse(BaseModel):
    id: int
    title: str
    description: str
    skills: List[str]  # ✅ Always return list of skills

    class Config:
        orm_mode = True
