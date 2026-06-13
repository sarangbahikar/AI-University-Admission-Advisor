import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

np.random.seed(42)

n = 1000

data = pd.DataFrame({
    "cgpa": np.random.uniform(5, 10, n),
    "ielts": np.random.uniform(5, 9, n),
    "experience": np.random.randint(0, 6, n),
    "projects": np.random.randint(0, 10, n),
    "research_papers": np.random.randint(0, 5, n),
    "certifications": np.random.randint(0, 8, n)
})

score = (
    data["cgpa"] * 8 +
    data["ielts"] * 5 +
    data["experience"] * 3 +
    data["projects"] * 2 +
    data["research_papers"] * 4 +
    data["certifications"] * 2
)

data["admitted"] = (
    score > 90
).astype(int)

X = data.drop("admitted", axis=1)
y = data["admitted"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

joblib.dump(
    model,
    "models/admission_model.pkl"
)

print("Model Saved Successfully")