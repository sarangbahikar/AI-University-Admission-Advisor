import streamlit as st
import pandas as pd

from utils.schema_mapper import detect_schema
from utils.recommendation_engine import recommend_universities

st.sidebar.success(
    "🎓 AI University Admission Advisor"
)

st.title("🏛️ University Recommendation Engine")

st.markdown(
    """
Upload a university dataset and receive personalized
recommendations based on your profile.
"""
)

uploaded_file = st.file_uploader(
    "Upload University Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Dataset Preview")

    st.dataframe(
        df.head()
    )

    if st.button(
        "🔍 Detect Schema & Recommend"
    ):

        with st.spinner(
            "Analyzing Dataset..."
        ):

            mapping = detect_schema(
                df
            )

        st.session_state["mapping"] = mapping

        st.success(
            "Schema Detected Successfully"
        )

        st.subheader(
            "Detected Schema"
        )

        st.json(
            mapping
        )

        if "profile" not in st.session_state:

            st.error(
                "Please save your profile first from the Student Profile page."
            )

        else:

            st.success(
                "Profile Loaded Successfully"
            )

            with st.expander(
                "👤 View Profile"
            ):

                st.json(
                    st.session_state["profile"]
                )

            recommendations = recommend_universities(
                df,
                mapping,
                st.session_state["profile"]
            )

            st.subheader(
                "🎓 Recommended Universities"
            )

            st.dataframe(
                recommendations,
                use_container_width=True
            )

            st.success(
                f"{len(recommendations)} universities matched your profile."
            )