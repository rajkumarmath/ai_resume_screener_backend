from sqlalchemy import Column, Integer, String, JSON
from app.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    skills = Column(JSON)   # ← FIXED
    embedding = Column(JSON)
