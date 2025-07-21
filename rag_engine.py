from llama_cpp import Llama
from langchain_community.vectorstores import FAISS

class RAGEngine:
    def __init__(self, model_path, vector_store):
        self.llm = Llama(model_path=model_path, n_ctx=2048, verbose=False)
        self.db = vector_store

    def query(self, user_question, k=3):
        # Step 1: Retrieve top-k relevant documents
        relevant_docs = self.db.similarity_search(user_question, k=k)
        context = "\n\n".join(doc.page_content for doc in relevant_docs)

        # Step 2: Format prompt
        prompt = f"""### System:
You are a helpful assistant that only answers based on the provided context.

### Context:
{context}

### Question:
{user_question}

### Answer:"""

        # Step 3: Query the local TinyLlama model
        response = self.llm(prompt, max_tokens=512, temperature=0.7)

        # Step 4: Extract and return the generated answer
        return response["choices"][0]["text"].strip()
