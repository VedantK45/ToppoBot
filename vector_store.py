# vector_store.py

import os
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# Use SentenceTransformer for embedding
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create a FAISS vector store from documents
def create_vector_store(docs):
    return FAISS.from_documents(docs, embeddings)

# ✅ THIS FUNCTION WAS MISSING EARLIER
def save_vector_store(vectorstore, save_path):
    os.makedirs(save_path, exist_ok=True)
    print(f"Saving FAISS index to: {save_path}")
    vectorstore.save_local(save_path)
    print(f"✅ Saved FAISS vector store at {save_path}")


# Load FAISS index from local folder
def load_vector_store(load_path):
    return FAISS.load_local(load_path, embeddings, allow_dangerous_deserialization=True)
