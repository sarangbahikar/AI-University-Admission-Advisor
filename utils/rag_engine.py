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


def add_document(text):

    embedding = model.encode(
        text
    ).tolist()

    collection.add(
        ids=[str(collection.count() + 1)],
        documents=[text],
        embeddings=[embedding]
    )


def retrieve(query, top_k=3):

    query_embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]