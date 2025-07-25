# vector_store.py

import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Use SentenceTransformer for embedding
embedding_model = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=embedding_model)

# ✅ Create a FAISS vector store from documents
def create_vector_store(docs):
    if not docs:
        raise ValueError("Document list is empty. Cannot create vector store.")
    return FAISS.from_documents(docs, embeddings)

# ✅ Save FAISS vector store to disk
def save_vector_store(vectorstore, save_path):
    os.makedirs(save_path, exist_ok=True)
    print(f"💾 Saving FAISS index to: {save_path}")
    vectorstore.save_local(save_path)
    print(f"✅ Vector store saved at: {save_path}")

# ✅ Load FAISS vector store from disk
def load_vector_store(load_path):
    if not os.path.exists(load_path):
        raise FileNotFoundError(f"Vector store not found at: {load_path}")
    print(f"📂 Loading FAISS index from: {load_path}")
    return FAISS.load_local(load_path, embeddings, allow_dangerous_deserialization=True)
