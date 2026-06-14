import streamlit as st
import time

from utils.pdf_parser import extract_text_from_pdf
from utils.rag_engine import (
    add_document,
    retrieve,
    clear_knowledge_base
)
from utils.rag_chat import answer_question

st.sidebar.success(
    "🎓 AI University Admission Advisor"
)

start = time.time()

st.title("🤖 University RAG Assistant")

st.info(
    "Upload university-related PDFs and ask questions using Retrieval-Augmented Generation (RAG)."
)

st.write(
    f"⚡ Page loaded in {round(time.time()-start, 2)} sec"
)

st.divider()

# -----------------------------
# Upload PDF
# -----------------------------

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text_from_pdf(
        uploaded_file
    )

    st.success(
        "PDF Processed Successfully"
    )

    if st.button(
        "📚 Add to Knowledge Base"
    ):

        with st.spinner(
            "Creating embeddings and storing document..."
        ):

            add_document(text)

        st.success(
            "Document Added Successfully"
        )

# -----------------------------
# Clear Database
# -----------------------------

if st.button(
    "🗑️ Clear Knowledge Base"
):

    with st.spinner(
        "Clearing database..."
    ):

        clear_knowledge_base()

    st.success(
        "Knowledge Base Cleared"
    )

st.divider()

# -----------------------------
# Ask Questions
# -----------------------------

question = st.text_input(
    "Ask a Question"
)

if st.button(
    "🔍 Get Answer"
):

    if question.strip() == "":

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Retrieving relevant information..."
        ):

            context = retrieve(
                question
            )

        with st.expander(
            "📄 Retrieved Context"
        ):

            st.write(
                context
            )

        with st.spinner(
            "Generating answer..."
        ):

            answer = answer_question(
                context,
                question
            )

        st.subheader(
            "🤖 Answer"
        )

        st.write(
            answer
        )