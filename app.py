import streamlit as st

st.set_page_config(
    page_title="AI University Admission Advisor",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI University Admission Advisor")

st.markdown("""
### Your AI-powered platform for international university admissions.

Features include:

- 📄 Resume Analysis
- 📝 SOP Analysis
- 🏛️ University Recommendations
- 📊 Admission Prediction
- 💰 Scholarship Advisor
- 🤖 RAG University Assistant
""")

st.divider()

# ------------------------
# Metrics
# ------------------------

profile_status = (
    "✅ Saved"
    if "profile" in st.session_state
    else "❌ Not Saved"
)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Profile",
        profile_status
    )

with col2:
    st.metric(
        "AI Modules",
        "6"
    )

with col3:
    st.metric(
        "Model R²",
        "0.7901"
    )

with col4:
    st.metric(
        "RAG",
        "Enabled"
    )

with col5:
    st.metric(
        "Dataset Engine",
        "Dynamic"
    )

st.divider()

st.subheader("🚀 Platform Modules")

modules = [
    "👤 Student Profile",
    "📄 Resume Analyzer",
    "📝 SOP Analyzer",
    "🏛️ University Recommendation Engine",
    "📊 Admission Predictor",
    "💰 Scholarship Advisor",
    "🤖 University RAG Assistant"
]

for module in modules:
    st.success(module)

st.divider()

st.subheader("📌 Workflow")

st.markdown("""
### Step 1
Create and save your student profile.

### Step 2
Upload university datasets and receive recommendations.

### Step 3
Analyze your Resume and SOP using GenAI.

### Step 4
Predict admission probability using a real ML model.

### Step 5
Discover scholarship opportunities.

### Step 6
Upload PDFs and query them using RAG.
""")

st.divider()

st.info(
    "Built using Streamlit, Groq, ChromaDB, Sentence Transformers, Scikit-Learn and Generative AI."
)