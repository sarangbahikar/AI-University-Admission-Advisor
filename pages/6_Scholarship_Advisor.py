import streamlit as st

from utils.scholarship_advisor import (
    recommend_scholarships
)

st.title("🎓 Scholarship Advisor")

if "profile" not in st.session_state:

    st.warning(
        "Please save profile first."
    )

else:

    profile = st.session_state["profile"]

    st.subheader("Current Profile")

    st.json(profile)

    if st.button(
        "Find Scholarships"
    ):

        with st.spinner(
            "Searching Scholarships..."
        ):

            result = recommend_scholarships(
                profile
            )

        st.subheader(
            "Scholarship Recommendations"
        )

        st.markdown(result)