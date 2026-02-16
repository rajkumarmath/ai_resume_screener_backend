import re

SKILL_KEYWORDS = [
    "python", "sql", "machine learning", "data analysis",
    "fastapi", "django", "pandas", "numpy", "tensorflow", "pytorch"
]

def extract_skills(text: str) -> list[str]:
    text = text.lower()
    skills = [skill for skill in SKILL_KEYWORDS if re.search(rf"\b{skill}\b", text)]
    return skills
