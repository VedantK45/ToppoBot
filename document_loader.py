import os
from langchain_community.document_loaders import PyPDFLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langdetect import detect

def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False

def clean_text(text):
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        line = line.strip()
        if line and is_english(line):
            cleaned.append(line)
    return " ".join(cleaned)

def load_documents(doc_dir):
    documents = []
    print(f"📁 Looking in: {doc_dir}")
    for filename in os.listdir(doc_dir):
        if filename.endswith(".pdf"):
            full_path = os.path.join(doc_dir, filename)
            print(f"📄 Loading: {full_path}")
            try:
                loader = PyPDFLoader(full_path)
                for doc in loader.load():
                    cleaned = clean_text(doc.page_content)
                    if cleaned.strip():
                        doc.page_content = cleaned
                        documents.append(doc)
            except Exception as e:
                print(f"❌ Failed to load {filename}: {e}")
    print(f"✅ Loaded {len(documents)} documents.")
    return documents


def split_documents(documents, chunk_size=200, chunk_overlap=20):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)
