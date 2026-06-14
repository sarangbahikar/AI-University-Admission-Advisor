import pandas as pd


def recommend_universities(df, mapping, profile):

    recommendations = []

    for _, row in df.iterrows():

        score = 0

        # English Test Match (IELTS-based datasets)

        try:

            if mapping.get("ielts"):

                required_english_score = float(
                    row[mapping["ielts"]]
                )

                if profile["english_test"] == "IELTS":

                    if profile["english_score"] >= required_english_score:
                        score += 35

                elif profile["english_test"] == "TOEFL":

                    # Approximate IELTS ↔ TOEFL conversion
                    # IELTS 6.5 ≈ TOEFL 90
                    # IELTS 7.0 ≈ TOEFL 100
                    # IELTS 7.5 ≈ TOEFL 105

                    estimated_ielts = (
                        profile["english_score"] / 15
                    )

                    if estimated_ielts >= required_english_score:
                        score += 35

        except:
            pass

        # CGPA Match

        try:

            if mapping.get("cgpa"):

                required_cgpa = float(
                    row[mapping["cgpa"]]
                )

                if profile["cgpa"] >= required_cgpa:
                    score += 35

        except:
            pass

        # Course Match

        try:

            if mapping.get("course"):

                student_course = (
                    profile["course"]
                    .lower()
                    .strip()
                )

                dataset_course = str(
                    row[mapping["course"]]
                ).lower()

                if student_course in dataset_course:
                    score += 30

        except:
            pass

        recommendations.append({

            "University":
                row[mapping["university"]],

            "Match Score":
                score,

            "Location":
                row[mapping["location"]]
                if mapping.get("location")
                else "N/A",

            "Tuition":
                row[mapping["tuition"]]
                if mapping.get("tuition")
                else "N/A"

        })

    recommendations = sorted(
        recommendations,
        key=lambda x: x["Match Score"],
        reverse=True
    )

    return pd.DataFrame(
        recommendations[:10]
    )