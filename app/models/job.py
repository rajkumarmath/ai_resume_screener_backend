# models/job.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import JSON
Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"
    __table_args__ = {"schema": "public"}


    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    skills = Column(String)  # stored as comma-separated string
    embedding = Column(JSON)


    @property
    def skills_list(self):
        return self.skills.split(",") if self.skills else []
