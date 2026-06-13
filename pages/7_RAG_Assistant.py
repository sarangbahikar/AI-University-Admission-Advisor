import streamlit as st

from utils.pdf_parser import extract_text_from_pdf
from utils.rag_engine import add_document
from utils.rag_engine import retrieve
from utils.rag_chat import answer_question

st.title("🤖 University RAG Assistant")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text_from_pdf(
        uploaded_file
    )

    if st.button("Add to Knowledge Base"):

        add_document(text)

        st.success(
            "Document Added Successfully"
        )

st.divider()

question = st.text_input(
    "Ask a Question"
)

if st.button("Get Answer"):

    context = retrieve(question)

    answer = answer_question(
        context,
        question
    )

    st.subheader("Answer")

    st.write(answer)