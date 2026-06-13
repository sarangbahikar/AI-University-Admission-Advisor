import streamlit as st
from utils.admission_predictor import predict_admission

st.title("📊 Admission Predictor")

if "profile" not in st.session_state:

    st.warning("Please save profile first.")

else:

    profile = st.session_state["profile"]

    st.subheader("Current Profile")

    st.json(profile)

    if st.button("Predict Admission Probability"):

        probability = predict_admission(profile)

        st.metric(
            "Admission Probability",
            f"{probability}%"
        )

        if probability >= 80:

            st.success("Strong Admission Profile")

            st.write("""
        ### Strengths

        ✅ Competitive academic profile

        ### Suggestions

        • Add certifications

        • Build more projects

        • Improve research exposure
        """)

        elif probability >= 60:

            st.warning("Moderate Admission Profile")

            st.write("""
        ### Suggestions

        • Increase project portfolio

        • Improve IELTS score

        • Obtain certifications
        """)

        else:

            st.error("Profile Needs Improvement")

            st.write("""
        ### Suggestions

        • Improve CGPA

        • Improve IELTS

        • Add projects and certifications
        """)