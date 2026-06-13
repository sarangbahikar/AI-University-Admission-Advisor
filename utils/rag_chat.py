from utils.groq_helper import get_groq_response


def answer_question(context, question):

    prompt = f"""
Answer using ONLY the provided context.

Context:
{context}

Question:
{question}

If answer not found, say:
'Information not found in uploaded documents.'
"""

    return get_groq_response(prompt)