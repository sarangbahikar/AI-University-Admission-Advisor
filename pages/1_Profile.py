import streamlit as st

st.sidebar.success("🎓 AI University Admission Advisor")

st.title("👤 Student Profile")

st.subheader("Academic Information")

name = st.text_input("Full Name")

course = st.selectbox(
    "Target Course",
    [
        "Data Science",
        "Artificial Intelligence",
        "Machine Learning",
        "Computer Science",
        "Business Analytics",
        "Cyber Security"
    ]
)

cgpa = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    step=0.1,
    value=7.0
)

english_test = st.radio(
    "English Proficiency Test",
    [
        "IELTS",
        "TOEFL"
    ]
)

if english_test == "IELTS":

    english_score = st.number_input(
        "IELTS Score",
        min_value=0.0,
        max_value=9.0,
        step=0.5
    )

else:

    english_score = st.number_input(
        "TOEFL Score",
        min_value=0,
        max_value=120,
        step=1
    )

st.subheader("Profile Strength")

experience = st.number_input(
    "Years of Experience",
    min_value=0,
    max_value=20,
    value=0
)

projects = st.number_input(
    "Number of Projects",
    min_value=0,
    max_value=100,
    value=0
)

research_papers = st.number_input(
    "Research Papers",
    min_value=0,
    max_value=50,
    value=0
)

certifications = st.number_input(
    "Certifications",
    min_value=0,
    max_value=100,
    value=0
)

if st.button("💾 Save Profile"):

    st.session_state["profile"] = {
        "name": name,
        "course": course,
        "cgpa": cgpa,
        "english_test": english_test,
        "english_score": english_score,
        "experience": experience,
        "projects": projects,
        "research_papers": research_papers,
        "certifications": certifications
    }

    st.success("Profile Saved Successfully!")

    st.subheader("Saved Profile")

    st.json(st.session_state["profile"])

# Show existing profile if already saved

if "profile" in st.session_state:

    st.divider()

    st.subheader("Current Active Profile")

    st.json(st.session_state["profile"])