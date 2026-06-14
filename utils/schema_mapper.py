import json
from utils.groq_helper import get_groq_response


def detect_schema(df):

    columns = df.columns.tolist()

    sample_data = df.head(5).to_dict()

    prompt = f"""
You are a data schema expert.

Dataset Columns:
{columns}

Sample Data:
{sample_data}

Identify the following fields:

1. university
2. ranking
3. tuition
4. ielts
5. course
6. location
7. cgpa

Return ONLY valid JSON.

Example:

{{
  "university":"College_Name",
  "ranking":"Ranking",
  "tuition":"Fees",
  "ielts":"English_Test",
  "course":"Course_Name",
  "location":"Location",
  "cgpa":"Minimum_CGPA"
}}
"""

    response = get_groq_response(prompt)

    try:

        # Remove markdown formatting if present
        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        mapping = json.loads(response)

        return mapping

    except Exception as e:

        return {
            "error": str(e),
            "raw_response": response
        }