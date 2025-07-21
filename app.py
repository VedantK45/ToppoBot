import streamlit as st
from vector_store import load_vector_store
from rag_engine import RAGEngine

st.set_page_config(page_title="ToppoBot", layout="wide")
st.title("🤖 ToppoBot - Product Bot From Toppan")

# ✅ Use the full path to the GGUF model file, not just the folder
MODEL_PATH = r"C:\Users\super\OneDrive\Documents\Desktop\ToppoBot\models\TinyLlama-1.1B-Chat-v1.0.Q4_K_M.gguf"

@st.cache_resource
def setup_rag():
    vector_store = load_vector_store("faiss_index")
    return RAGEngine(MODEL_PATH, vector_store)

rag = setup_rag()

query = st.text_input("Greetings From ToppoBot!", placeholder="Ask something about our products:")
if st.button("Submit") and query:
    with st.spinner("Thinking..."):
        answer = rag.query(query)
    st.markdown("### Answer:")
    st.write(answer)
