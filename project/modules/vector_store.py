import os
import pdfplumber
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

PDF_STORAGE_PATH = "data"
CHROMA_DB_PATH = "chroma_db"
EMBEDDING_MODEL = OllamaEmbeddings(model="nomic-embed-text")

def load_pdf_text(file_path):
    """Extracts text from a PDF file."""
    with pdfplumber.open(file_path) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

def store_vectors():
    """Extracts text from PDFs, generates embeddings, and stores them in ChromaDB."""
    documents = []
    metadata_list = []

    for file_name in os.listdir(PDF_STORAGE_PATH):
        file_path = os.path.join(PDF_STORAGE_PATH, file_name)
        text = load_pdf_text(file_path)
        documents.append(text)
        metadata_list.append({"source": file_name})

    print("📥 Embedding and storing documents into ChromaDB...")

    vector_db = Chroma.from_texts(
        documents,
        EMBEDDING_MODEL,
        metadatas=metadata_list,
        persist_directory=CHROMA_DB_PATH
    )

    vector_db.persist()
    print("✅ Documents successfully stored in vector database.")

def load_vector_db():
    """Loads the stored embeddings from ChromaDB."""
    return Chroma(persist_directory=CHROMA_DB_PATH, embedding_function=EMBEDDING_MODEL)

def find_related_documents(vector_db, query):
    """Finds the most relevant document for a given query."""
    results = vector_db.similarity_search(query, k=1)  # Retrieve top 1 match
    if results:
        return results[0].page_content, results[0].metadata["source"]
    return "No relevant document found.", None
