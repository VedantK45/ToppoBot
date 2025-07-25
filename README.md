# 🤖 ToppoBot – Offline RAG-Based Document Chatbot

ToppoBot is a locally running document-based chatbot that uses **Retrieval-Augmented Generation (RAG)** to answer queries from internal company documents (PDFs, TXT, DOCX). It is designed for enterprise environments where data privacy and offline access are critical.

---

## 🚀 Features

- ✅ **Document-based Q&A**: Answers questions from uploaded internal documents.
- 📄 **Multi-format Loader**: Supports PDF, DOCX, and TXT files.
- 🧠 **Semantic Search**: Uses FAISS + sentence transformers for high-quality chunk retrieval.
- 💬 **Conversational Chat UI**: Built with Streamlit for a clean, chat-like interface.
- 🏭 **Enterprise-Ready**: Designed for internal usage in companies like film manufacturing firms.
- 🔌 **API-based (Groq/OpenAI/Mistral optional)** or completely **offline LLM** using GGUF models.

---

## 🗂️ Project Structure

```
ToppoBot/
├── app.py                # Streamlit frontend
├── document_loader.py    # Loads and cleans documents
├── vector_store.py       # Builds FAISS vector index
├── rag_engine.py         # Handles query answering logic
├── generate_index.py     # CLI to build or update the vector store
├── requirements.txt      # Python dependencies
├── .env                  # API keys (excluded from GitHub)
└── venv/                 # Virtual environment (excluded from GitHub)
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ToppoBot.git
cd ToppoBot
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Add Your API Key (Optional)

Create a `.env` file and add:

```env
GROQ_API_KEY=your_groq_key_here
```

---

## 🧠 How It Works

- **Document Loader**: Cleans and chunks the document text.
- **Vector Store**: Builds a FAISS index from those chunks.
- **RAG Engine**: Retrieves relevant chunks and generates an answer using the LLM.
- **UI**: Streamlit provides a chat-like interface.

---

## 🧪 Example Usage

```bash
# Index your documents
python generate_index.py

# Launch chatbot
streamlit run app.py
```

---

## 🔐 Security & Privacy

- No data is sent outside if using offline LLMs.
- `.env` and `venv/` are excluded from version control using `.gitignore`.

---

## 🔮 Future Improvements

- [ ] Add feedback & rating system for answers
- [ ] Support document upload via UI
- [ ] Summarization of large documents
- [ ] Multilingual support

---

## 🤝 Acknowledgements

Built by **Vedant Kumar** and **Gauri Verma**, Interns at **Toppan Films**, as part of an enterprise-grade automation initiative.

---
