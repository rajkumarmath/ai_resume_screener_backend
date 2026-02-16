import os
from dotenv import load_dotenv

load_dotenv()  # optional locally

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/resume_db")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

settings = Settings()
