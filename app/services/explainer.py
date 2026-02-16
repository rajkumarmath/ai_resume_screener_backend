import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

def generate_explanation(job_text: str, resume_text: str, score: float):

    prompt = f"""
You are an AI hiring assistant.

Job Description:
{job_text}

Resume:
{resume_text}

Similarity Score: {score:.3f}

Explain in a structured way:
1. Why this candidate matches the role, if he does/else explain y he does'nt
2. Key overlapping skills
3. Missing or weak areas
4. Overall evaluation (2-3 sentences max)

Keep response concise and professional.
"""

    response = model.generate_content(prompt)
    return response.text
