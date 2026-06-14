import pandas as pd


def recommend_universities(df, mapping, profile):

    recommendations = []

    for _, row in df.iterrows():

        score = 0

        reasons = []

        # ------------------------
        # English Test Match
        # ------------------------

        try:

            required_score = float(
                row[mapping["ielts"]]
            )

            if profile["english_test"] == "IELTS":

                if profile["english_score"] >= required_score:

                    score += 20

                    reasons.append(
                        "English requirement satisfied"
                    )

            elif profile["english_test"] == "TOEFL":

                estimated_ielts = (
                    profile["english_score"] / 15
                )

                if estimated_ielts >= required_score:

                    score += 20

                    reasons.append(
                        "English requirement satisfied"
                    )

        except:
            pass

        # ------------------------
        # CGPA Match
        # ------------------------

        try:

            required_cgpa = float(
                row[mapping["cgpa"]]
            )

            cgpa_difference = (
                profile["cgpa"] - required_cgpa
            )

            if cgpa_difference >= 1:

                score += 30

                reasons.append(
                    "Strong CGPA advantage"
                )

            elif cgpa_difference >= 0:

                score += 20

                reasons.append(
                    "Meets CGPA requirement"
                )

        except:
            pass

        # ------------------------
        # Course Match
        # ------------------------

        try:

            student_course = (
                profile["course"]
                .lower()
                .strip()
            )

            dataset_course = str(
                row[mapping["course"]]
            ).lower()

            if student_course in dataset_course:

                score += 20

                reasons.append(
                    "Course match"
                )

        except:
            pass

        # ------------------------
        # Ranking Bonus
        # ------------------------

        try:

            ranking = int(
                row[mapping["ranking"]]
            )

            if ranking <= 20:

                score += 15

                reasons.append(
                    "Top-ranked university"
                )

            elif ranking <= 50:

                score += 10

            elif ranking <= 100:

                score += 5

        except:
            pass

        # ------------------------
        # Scholarship Bonus
        # ------------------------

        try:

            scholarship = str(
                row["Scholarship_Available"]
            ).lower()

            if scholarship == "yes":

                score += 10

                reasons.append(
                    "Scholarship available"
                )

        except:
            pass

        # ------------------------
        # Profile Strength Bonus
        # ------------------------

        profile_strength = (
            profile["projects"]
            + profile["research_papers"]
            + profile["certifications"]
        )

        if profile_strength >= 10:

            score += 5

            reasons.append(
                "Strong extracurricular profile"
            )

        recommendations.append({

            "University":
                row[mapping["university"]],

            "Match Score":
                score,

            "Ranking":
                row[mapping["ranking"]]
                if mapping.get("ranking")
                else "N/A",

            "Tuition":
                row[mapping["tuition"]]
                if mapping.get("tuition")
                else "N/A",

            "Location":
                row[mapping["location"]]
                if mapping.get("location")
                else "N/A",

            "Scholarship":
                row["Scholarship_Available"]
                if "Scholarship_Available" in row
                else "N/A",

            "Reason":
                ", ".join(reasons)
        })

    recommendations = sorted(
        recommendations,
        key=lambda x: x["Match Score"],
        reverse=True
    )

    return pd.DataFrame(
        recommendations[:10]
    )