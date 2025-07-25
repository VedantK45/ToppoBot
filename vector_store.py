import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# ✅ Use same model used to originally create FAISS
embedding_model = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=embedding_model)

# ✅ Load existing FAISS vector store from disk
def load_vector_store(load_path):
    if not os.path.exists(load_path):
        raise FileNotFoundError(f"Vector store not found at: {load_path}")
    print(f"📂 Loading FAISS index from: {load_path}")
    return FAISS.load_local(load_path, embeddings, allow_dangerous_deserialization=True)
