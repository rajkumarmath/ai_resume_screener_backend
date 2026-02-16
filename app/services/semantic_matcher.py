from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_similarity(resume_text: str, job_description: str) -> float:
    embeddings_resume = model.encode(resume_text, convert_to_tensor=True)
    embeddings_job = model.encode(job_description, convert_to_tensor=True)
    score = util.cos_sim(embeddings_resume, embeddings_job).item()
    return score
