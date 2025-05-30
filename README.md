# Resume Matcher 🧠📄

A machine learning–powered resume analyzer that compares resumes to job descriptions using semantic similarity and skill matching.

## 🚀 Features

- Skill extraction from resumes and job descriptions
- Semantic similarity scoring using TF-IDF & cosine similarity
- Combined score for better accuracy
- REST API using Flask
- Ready to integrate with a React frontend

## 📂 API Endpoint

**POST** `/analyze`

| Parameter      | Type     | Description                    |
|----------------|----------|--------------------------------|
| `resume`       | File     | PDF file of the resume         |
| `job`          | File     | DOCX file of the job description |

Returns a JSON response like:

```json
{
  "resume_skills": [...],
  "job_skills": [...],
  "semantic_score": 71.6,
  "combined_score": 73.98
}
