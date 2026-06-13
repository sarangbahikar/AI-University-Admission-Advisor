import streamlit as st
st.sidebar.success("🎓 AI University Admission Advisor")
from utils.pdf_parser import extract_text_from_pdf
from utils.resume_analyzer import analyze_resume

st.title("📄 Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("Extracting Resume Text..."):

        resume_text = extract_text_from_pdf(
            uploaded_file
        )

    st.subheader("Resume Preview")

    st.text_area(
        "Extracted Text",
        resume_text[:3000],
        height=250
    )

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            analysis = analyze_resume(
                resume_text
            )

        st.subheader("AI Resume Analysis")

        st.markdown(analysis)