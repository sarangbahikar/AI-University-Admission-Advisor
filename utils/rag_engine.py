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


model, collection = get_rag_resources()


# --------------------------------
# Text Chunking
# --------------------------------

def chunk_text(
    text,
    chunk_size=500,
    overlap=100
):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


# --------------------------------
# Store Chunks
# --------------------------------

def add_document(text):

    chunks = chunk_text(text)

    current_count = collection.count()

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
# Retrieve Relevant Chunks
# --------------------------------

def retrieve(
    query,
    top_k=5
):

    query_embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=top_k
    )

    documents = results["documents"][0]

    return "\n\n".join(documents)