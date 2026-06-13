import joblib
import pandas as pd

model = joblib.load(
    "models/admission_model.pkl"
)

def predict_admission(profile):

    df = pd.DataFrame([{
        "cgpa": profile["cgpa"],
        "ielts": profile["ielts"],
        "experience": profile["experience"],
        "projects": profile["projects"],
        "research_papers": profile["research_papers"],
        "certifications": profile["certifications"]
    }])

    probability = model.predict_proba(df)[0][1]

    return round(probability * 100, 2)