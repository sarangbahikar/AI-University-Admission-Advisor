import streamlit as st

from utils.pdf_parser import extract_text_from_pdf
from utils.sop_analyzer import analyze_sop
st.sidebar.success("🎓 AI University Admission Advisor")
st.title("📝 SOP Analyzer")

uploaded_file = st.file_uploader(
    "Upload SOP PDF",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("Extracting SOP Text..."):

        sop_text = extract_text_from_pdf(
            uploaded_file
        )

    st.subheader("SOP Preview")

    st.text_area(
        "Extracted SOP",
        sop_text[:4000],
        height=300
    )

    if st.button("Analyze SOP"):

        with st.spinner("Analyzing SOP..."):

            result = analyze_sop(
                sop_text
            )

        st.subheader("AI SOP Analysis")

        st.markdown(result)