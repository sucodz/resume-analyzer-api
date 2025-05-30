def score_resume(resume_info, job_info, semantic_score, alpha=0.6):
    # alpha = weight for skills score
    resume_skills = set(resume_info.get("skills_resume", []))
    job_skills = set(job_info.get("skills_job", []))

    if not job_skills:
        return 0.0

    matched = resume_skills & job_skills
    skills_score = len(matched) / len(job_skills)  # ratio [0,1]

    # Combine weighted scores (skills + semantic similarity scaled [0,1])
    combined_score = alpha * skills_score + (1 - alpha) * (semantic_score / 100)

    return round(combined_score * 100, 2)






# # scoring.py

# def improved_score(resume_info, job_info, semantic_score, skill_weight=0.8, semantic_weight=0.2):
#     resume_skills = set(resume_info.get("skills_resume", []))
#     job_skills = set(job_info.get("skills_job", []))

#     if not job_skills:
#         return semantic_score  # fallback to semantic only if no skills

#     matched_skills = resume_skills & job_skills
#     skill_match_ratio = len(matched_skills) / len(job_skills)

#     skill_score = skill_match_ratio * 100  # scale to 0-100

#     combined_score = skill_score * skill_weight + semantic_score * semantic_weight

#     return round(combined_score, 2)
