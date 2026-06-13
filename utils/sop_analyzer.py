from utils.groq_helper import get_groq_response

def analyze_sop(sop_text):

    prompt = f"""
You are an expert UK university admission consultant.

Analyze the following Statement of Purpose (SOP).

SOP:
{sop_text}

Evaluate:

1. Overall SOP Score (out of 100)
2. Motivation and Career Goals
3. Academic Strength
4. Research Interest
5. Writing Quality
6. University Fit
7. Strengths
8. Weaknesses
9. Suggestions for Improvement

Return the result in professional markdown format.
"""

    return get_groq_response(prompt)