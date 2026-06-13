import streamlit as st
import pandas as pd

from utils.schema_mapper import detect_schema
from utils.recommendation_engine import recommend_universities
st.sidebar.success("🎓 AI University Admission Advisor")
st.title("🏛️ University Recommendation Engine")

# Debug Session State
st.subheader("🔍 Session State Debug")
st.write(st.session_state)

uploaded_file = st.file_uploader(
    "Upload University Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    if st.button("Detect Schema"):

        with st.spinner("Analyzing Dataset..."):

            mapping = detect_schema(df)

        st.session_state["mapping"] = mapping

        st.success("Schema Detected Successfully")

        st.subheader("Detected Schema")

        st.json(mapping)

        # Check Profile Exists
        if "profile" not in st.session_state:

            st.error("❌ Profile not found in Session State")

            st.write("Current Session State:")

            st.json(dict(st.session_state))

        else:

            st.success("✅ Profile Found")

            st.subheader("Current Profile")

            st.json(st.session_state["profile"])

            recommendations = recommend_universities(
                df,
                mapping,
                st.session_state["profile"]
            )

            st.subheader("🎓 Recommended Universities")

            st.dataframe(recommendations)