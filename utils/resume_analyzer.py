from utils.groq_helper import get_groq_response


def analyze_resume(resume_text):

    prompt = f"""
You are an expert university admission advisor.

Analyze the following resume.

Resume:
{resume_text}

Provide:

1. Resume Score (out of 100)
2. Strengths
3. Weaknesses
4. Missing Skills
5. Recommendations

Return in clear markdown format.
"""

    return get_groq_response(prompt)