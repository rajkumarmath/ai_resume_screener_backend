from sqlalchemy import Column, Integer, String, JSON, Text
from app.database import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    name = Column(String)
    content = Column(Text)   # FULL RESUME TEXT
    skills = Column(JSON)
    embedding = Column(JSON)
