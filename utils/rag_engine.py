import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer


@st.cache_resource
def get_rag_resources():

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    client = chromadb.PersistentClient(
        path="chroma_db"
    )

    collection = client.get_or_create_collection(
        name="university_docs"
    )

    return model, collection


# --------------------------------
# Text Chunking
# --------------------------------

def chunk_text(
    text,
    chunk_size=300,
    overlap=50
):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunks.append(
            text[start:end]
        )

        start += (
            chunk_size - overlap
        )

    return chunks


# --------------------------------
# Store Chunks
# --------------------------------

def add_document(text):

    model, collection = (
        get_rag_resources()
    )

    chunks = chunk_text(text)

    current_count = (
        collection.count()
    )

    for i, chunk in enumerate(chunks):

        embedding = model.encode(
            chunk
        ).tolist()

        collection.add(
            ids=[
                f"{current_count}_{i}"
            ],
            documents=[chunk],
            embeddings=[embedding]
        )


# --------------------------------
# Retrieve Chunks
# --------------------------------

def retrieve(
    query,
    top_k=3
):

    model, collection = (
        get_rag_resources()
    )

    query_embedding = (
        model.encode(query)
        .tolist()
    )

    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=top_k
    )

    documents = (
        results["documents"][0]
    )

    return "\n\n".join(
        documents
    )


# --------------------------------
# Clear Knowledge Base
# --------------------------------

def clear_knowledge_base():

    client = chromadb.PersistentClient(
        path="chroma_db"
    )

    try:

        client.delete_collection(
            "university_docs"
        )

    except:
        pass

    client.get_or_create_collection(
        name="university_docs"
    )