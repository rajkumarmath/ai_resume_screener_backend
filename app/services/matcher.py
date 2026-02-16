def calculate_match_score(resume_skills, job_description):
    job_description = job_description.lower()

    match_count = 0
    for skill in resume_skills:
        if skill in job_description:
            match_count += 1

    if len(resume_skills) == 0:
        return 0

    score = (match_count / len(resume_skills)) * 100
    return round(score, 2)
