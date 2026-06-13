from utils.groq_helper import get_groq_response


def recommend_scholarships(profile):

    prompt = f"""
You are a UK university scholarship advisor.

Student Profile:

Name: {profile['name']}
Course: {profile['course']}
CGPA: {profile['cgpa']}
IELTS: {profile['ielts']}
Experience: {profile['experience']}
Projects: {profile['projects']}
Research Papers: {profile['research_papers']}
Certifications: {profile['certifications']}

Recommend:

1. Suitable UK Scholarships
2. Eligibility Match
3. Scholarship Amount
4. Why Recommended
5. Application Tips

Focus on:
- Chevening Scholarship
- Commonwealth Scholarship
- GREAT Scholarship
- University-specific scholarships

Return in professional markdown format.
"""

    return get_groq_response(prompt)