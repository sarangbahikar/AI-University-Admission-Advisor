import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

df = pd.read_csv(
    "datasets/Admission_Predict_Ver1.1.csv"
)

df.columns = df.columns.str.strip()
print(df.columns.tolist())  
X = df[
    [
        "GRE Score",
        "TOEFL Score",
        "University Rating",
        "SOP",
        "LOR",
        "CGPA",
        "Research"
    ]
]

y = df["Chance of Admit"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = r2_score(
    y_test,
    predictions
)

print(
    f"Model R² Score: {accuracy:.4f}"
)

joblib.dump(
    model,
    "models/admission_model.pkl"
)

with open(
    "models/model_metrics.txt",
    "w"
) as f:

    f.write(
        f"R2 Score: {accuracy:.4f}"
    )
    
print(
    "Model Saved Successfully"
)

sample = pd.DataFrame([{
    "GRE Score": 290,
    "TOEFL Score": 85,
    "University Rating": 2,
    "SOP": 2,
    "LOR": 2,
    "CGPA": 6.5,
    "Research": 0
}])

print("Test Prediction:", model.predict(sample)[0])