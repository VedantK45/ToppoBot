import os
from langchain.prompts import PromptTemplate
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_api_key = st.secrets["GROQ_API_KEY"]

if not groq_api_key:
    raise ValueError("❌ GROQ_API_KEY is not set. Please check your .env file or environment variables.")

class GroqLLMWrapper:
    def __init__(self, model="llama3-70b-8192"):
        self.client = Groq(api_key=groq_api_key)
        self.model = model

    def __call__(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": (
                        "You are a highly accurate assistant specialized in internal manufacturing documentation. "
                        "Your answers MUST be based only on the provided context. If something is not mentioned, respond with: 'Not mentioned in context.' "
                        "Be concise, specific, data-driven (mention specs, numbers, grades, codes), and capable of responding to technical and non-technical questions alike."
                    )},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=1000,
                top_p=1.0
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"⚠️ Groq Mistral error: {str(e)}"


class RAGEngine:
    def __init__(self, vector_store):
        self.vector_store = vector_store

        prompt_template = """
You are a highly specialized assistant for internal manufacturing documents and product catalogs.

🎯 **Rules:**
- ONLY use the given context.
- If the user asks something unrelated to product data (e.g., "Who is the PM of India?"), say: **"Not mentioned in context."**
- If asked about product applications (e.g., for bakery, food packaging, etc.), use contextual information to recommend options.
- If no suitable data is found, respond gracefully and suggest what the user can ask next.

🔍 **Formatting:**
- ✅ Use markdown bullet points and tables for clarity.
- 📊 Prefer structured sections and columns (like grade, thickness, application, etc.)
- 🚫 Do not hallucinate. Stick strictly to available data.
- 💬 Ask a **clarifying follow-up question** based on user’s query to guide next steps.

---

📚 **Context**:
{context}

❓ **User Question**:
{question}

---

### ✅ Structured Answer

### 🧾 Overview
- ...

### 🧰 Applications / Use Cases
| Application Area | Suitable Grades / Types | Features |
|------------------|-------------------------|----------|
| ...              | ...                     | ...      |

### 📏 Dimensions / Grades Table
If tables are present in the context, extract and reformat them. Preserve units (e.g., µm, g/m²) and column names.
[TABLE: SPECIFICATIONS]
| Grade | Thickness (µm) | Yield (m²/kg) | Grammage (g/m²) | Type | Features |
|-------|----------------|---------------|------------------|------|----------|
| ...   | ...            | ...           | ...              | ...  | ...      |

### 📦 Packaging / Storage
- ...

### ⚙️ Technical Details
- ...

---

💡 **Next Step Suggestion**:
Based on your question, you might also ask:
- {clarifying_question}
"""

        self.prompt = PromptTemplate(
            input_variables=["context", "question", "clarifying_question"],
            template=prompt_template
        )

        self.llm = GroqLLMWrapper()

    def query(self, question):
        try:
            docs = self.vector_store.similarity_search(question, k=3)

            # Structured context with document headers
            context = ""
            for i, doc in enumerate(docs, 1):
                context += f"\n\n📄 **Document {i}:**\n{doc.page_content.strip()}"

            # Hallucination guard: unrelated queries
            unrelated_keywords = ["prime minister", "president", "weather", "movie", "actor", "cricket"]
            if any(keyword in question.lower() for keyword in unrelated_keywords):
                return "**Not mentioned in context.**"

            # Dynamic clarifying question generation (simple heuristic)
            if "application" in question.lower() or "use" in question.lower():
             followup = "Would you like suggestions for alternative applications or performance under specific conditions?"
            elif "grade" in question.lower() or "thickness" in question.lower():
                followup = "Do you want help comparing grades or understanding thickness/yield trade-offs?"
            elif "storage" in question.lower():
                followup = "Would you like to know how long it can be stored or at what temperature?"
            else:
                followup = "Would you like help with comparisons, variants, or use-case suitability?"

            prompt = self.prompt.format(
            context=context,
            question=question,
            clarifying_question=followup
            )
            return self.llm(prompt)

        except Exception as e:
            return f"⚠️ RAG error: {str(e)}"
        
