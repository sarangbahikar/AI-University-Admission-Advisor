import streamlit as st

st.set_page_config(
    page_title="AI University Admission Advisor",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI University Admission Advisor")

st.markdown("""
Your AI-powered platform for:

- 🎓 University Recommendations
- 📄 Resume Analysis
- 📝 SOP Analysis
- 📊 Admission Prediction
- 💰 Scholarship Recommendations
- 🤖 RAG-based University Assistant
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:

    profile_status = (
        "✅ Saved"
        if "profile" in st.session_state
        else "❌ Not Saved"
    )

    st.metric(
        "Profile Status",
        profile_status
    )

with col2:

    st.metric(
        "AI Modules",
        "6"
    )

with col3:

    st.metric(
        "Project Version",
        "1.0"
    )

st.divider()

st.subheader("🚀 Features")

features = [
    "Student Profile",
    "Resume Analyzer",
    "SOP Analyzer",
    "University Recommendation Engine",
    "Admission Predictor",
    "Scholarship Advisor",
    "ChromaDB RAG Assistant"
]

for feature in features:
    st.success(feature)

st.divider()

st.subheader("📌 How To Use")

st.markdown("""
### Step 1
Save your profile.

### Step 2
Upload university dataset and get recommendations.

### Step 3
Analyze Resume and SOP.

### Step 4
Predict admission probability.

### Step 5
Discover scholarships.

### Step 6
Use the AI RAG Assistant to ask questions from uploaded PDFs.
""")

st.divider()

st.info(
    "Built using Streamlit, Groq, ChromaDB, Scikit-Learn and Generative AI."
)