import joblib
import pandas as pd

model = joblib.load(
    "models/admission_model.pkl"
)
print("REAL MODEL LOADED")
def predict_admission(data):

    df = pd.DataFrame([{
        "GRE Score": data["gre"],
        "TOEFL Score": data["toefl"],
        "University Rating": data["university_rating"],
        "SOP": data["sop"],
        "LOR": data["lor"],
        "CGPA": data["cgpa"],
        "Research": data["research"]
    }])

    prediction = model.predict(df)[0]

    return round(prediction * 100, 2)