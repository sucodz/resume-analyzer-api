from semantic_matcher import get_similarity
from scoring import score_resume
from text_extractors import extract_text_from_pdf, extract_text_from_docx
from skill_extractor import extract_skills_from_text

def analyze_resume(resume_file, job_file):
    resume_text = extract_text_from_pdf(resume_file)
    job_text = extract_text_from_docx(job_file)

    resume_skills = extract_skills_from_text(resume_text)
    job_skills = extract_skills_from_text(job_text)

    semantic_score = get_similarity(resume_text, job_text)

    combined_score = score_resume(
        {"skills_resume": resume_skills},
        {"skills_job": job_skills},
        semantic_score,
        alpha=0.7
    )

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "semantic_score": semantic_score,
        "combined_score": combined_score
    }








# # analyze_resume.py

# from text_extractors import extract_text_from_pdf, extract_text_from_docx
# from skill_extractor import extract_skills_from_text
# from semantic_matcher import get_similarity
# from scoring import improved_score

# def analyze_resume(resume_file, job_file):
#     resume_text = extract_text_from_pdf(resume_file)
#     job_text = extract_text_from_docx(job_file)

#     resume_skills = extract_skills_from_text(resume_text)
#     job_skills = extract_skills_from_text(job_text)

#     semantic_score = get_similarity(resume_text, job_text)

#     combined_score = improved_score(
#         {'skills_resume': resume_skills},
#         {'skills_job': job_skills},
#         semantic_score
#     )

#     return {
#         "resume_skills": resume_skills,
#         "job_skills": job_skills,
#         "semantic_score": semantic_score,
#         "score": combined_score
#     }








# # analyze_resume.py
# from text_extractors import extract_text_from_pdf, extract_text_from_docx
# from skill_extractor import extract_skills_from_text
# from semantic_matcher import get_similarity

# def analyze_resume(resume_file, job_file):
#     resume_text = extract_text_from_pdf(resume_file)
#     job_text = extract_text_from_docx(job_file)

#     resume_skills = extract_skills_from_text(resume_text)
#     job_skills = extract_skills_from_text(job_text)

#     semantic_score = get_similarity(resume_text, job_text)

#     return {
#         "resume_skills": resume_skills,
#         "job_skills": job_skills,
#         "semantic_score": semantic_score
#     }











# # analyze_resume.py
# # analyze_resume.py

# from text_extractors import extract_text_from_pdf, extract_text_from_docx
# from skill_extractor import extract_skills_from_text
# from semantic_matcher import get_similarity

# def analyze_resume(resume_file_path, job_file_path):
#     resume_text = extract_text_from_pdf(resume_file_path)
#     job_text = extract_text_from_docx(job_file_path)

#     resume_skills = extract_skills_from_text(resume_text)
#     job_skills = extract_skills_from_text(job_text)

#     semantic_score = get_similarity(resume_text, job_text)

#     return {
#         "resume_skills": resume_skills,
#         "job_skills": job_skills,
#         "semantic_score": semantic_score
#     }

# Example use (you can remove this when using in Flask/FastAPI):
# if __name__ == "__main__":
#     result = analyze_resume("my_resume.pdf", "job_description.docx")
#     print("Resume skills:", result["resume_skills"])
#     print("Job skills:", result["job_skills"])
#     print("Semantic score:", result["semantic_score"], "%")









# from text_extractors import extract_text_from_pdf, extract_text_from_docx
# from skill_extractor import extract_skills_from_text
# from semantic_matcher import get_similarity

# resume_text = extract_text_from_pdf("my_resume.pdf")
# job_text = extract_text_from_docx("job_description.docx")

# resume_skills = extract_skills_from_text(resume_text)
# job_skills = extract_skills_from_text(job_text)

# semantic_score = get_similarity(resume_text, job_text)

# print("Resume skills:", resume_skills)
# print("Job skills:", job_skills)
# print("Semantic score:", semantic_score, "%")
