from document_loader import load_documents, split_documents
from vector_store import create_vector_store, save_vector_store

docs = load_documents(r"C:\Users\super\OneDrive\Documents\Desktop\ToppoBot\documents")
print(f"Loaded {len(docs)} documents.")

chunks = split_documents(docs)
print(f"Split into {len(chunks)} chunks.")

vs = create_vector_store(chunks)
save_vector_store(vs, "faiss_index")
print("✅ FAISS vector store saved.")
