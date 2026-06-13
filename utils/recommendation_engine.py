import pandas as pd

def recommend_universities(df, mapping, profile):

    recommendations = []

    for _, row in df.iterrows():

        score = 0

        # IELTS Score
        if "ielts" in mapping:

            try:
                required_ielts = float(row[mapping["ielts"]])

                if profile["ielts"] >= required_ielts:
                    score += 40

            except:
                pass

        # CGPA Score
        if "Min_CGPA" in df.columns:

            try:
                min_cgpa = float(row["Min_CGPA"])

                if profile["cgpa"] >= min_cgpa:
                    score += 40

            except:
                pass

        # Course Match
        if "course" in mapping:

            try:

                if profile["course"].lower() in str(
                    row[mapping["course"]]
                ).lower():

                    score += 20

            except:
                pass

        recommendations.append({
            "University": row[mapping["university"]],
            "Match Score": score
        })

    recommendations = sorted(
        recommendations,
        key=lambda x: x["Match Score"],
        reverse=True
    )

    return recommendations[:10]