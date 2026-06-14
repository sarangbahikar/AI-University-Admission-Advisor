import streamlit as st

from utils.admission_predictor import (
    predict_admission
)

st.sidebar.success(
    "🎓 AI University Admission Advisor"
)

st.title("📊 Advanced Admission Predictor")

with open(
    "models/model_metrics.txt",
    "r"
) as f:

    metric = f.read()

st.info(
    f"Model Performance: {metric}"
)

st.markdown(
    "Predict admission probability using a model trained on a real graduate admissions dataset."
)

gre = st.slider(
    "GRE Score",
    260,
    340,
    310
)

toefl = st.slider(
    "TOEFL Score",
    80,
    120,
    100
)

university_rating = st.slider(
    "University Rating",
    1,
    5,
    3
)

sop = st.slider(
    "SOP Strength",
    1.0,
    5.0,
    3.0,
    0.5
)

lor = st.slider(
    "LOR Strength",
    1.0,
    5.0,
    3.0,
    0.5
)

cgpa = st.slider(
    "CGPA",
    0.0,
    10.0,
    8.0,
    0.1
)

research = st.selectbox(
    "Research Experience",
    [0, 1]
)

if st.button(
    "Predict Admission Chance"
):

    probability = predict_admission({
        "gre": gre,
        "toefl": toefl,
        "university_rating": university_rating,
        "sop": sop,
        "lor": lor,
        "cgpa": cgpa,
        "research": research
    })

    st.metric(
        "Admission Probability",
        f"{probability}%"
    )

    if probability >= 80:

        st.success(
            "Excellent Admission Prospects"
        )

    elif probability >= 60:

        st.warning(
            "Moderate Admission Prospects"
        )

    else:

        st.error(
            "Admission Chances Need Improvement"
        )