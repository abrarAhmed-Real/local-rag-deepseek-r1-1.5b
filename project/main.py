import os
from modules.pdf_generator import create_pdfs
from modules.vector_store import store_vectors
from modules.query_handler import query_model
print('add something')
if __name__ == "__main__":
    """Run this script once to generate PDFs and store vectors. Then use query_model() separately."""
    if not os.path.exists("data"):
        create_pdfs()
        store_vectors()

    query_model()  # Runs interactive querying

 
