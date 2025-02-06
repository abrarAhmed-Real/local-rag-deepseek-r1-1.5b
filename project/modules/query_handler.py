from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from modules.vector_store import load_vector_db, find_related_documents

LANGUAGE_MODEL = OllamaLLM(model="deepseek-r1:1.5b")

def generate_answer_stream(user_query, doc_text, doc_source):
    """Streams the AI response token by token based on retrieved document context."""
    PROMPT_TEMPLATE = """
    You are an AI assistant with access to relevant documents.
    Answer the query using the provided document context only in 50 words.
    If the document does not contain relevant information, state that you don't know.

    Query: {user_query}
    Document Source: {doc_source}
    Document Context: {doc_text}

    Answer:
    """

    conversation_prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    response_chain = conversation_prompt | LANGUAGE_MODEL

    for chunk in response_chain.stream({"user_query": user_query, "doc_source": doc_source, "doc_text": doc_text}):
        print(chunk, end="", flush=True)

def query_model():
    """Handles user queries by retrieving relevant documents and generating AI responses."""
    vector_db = load_vector_db()

    while True:
        user_query = input("\n❓ Ask a question (or type 'exit' to quit): ").strip()
        if user_query.lower() == "exit":
            print("👋 Exiting. Have a great day!")
            break

        print("\n🔍 Searching for relevant document...")
        doc_text, doc_source = find_related_documents(vector_db, user_query)

        if doc_source:
            print(f"\n📄 Matched Document: {doc_source}")
            print("🤖 Generating response...\n")
            generate_answer_stream(user_query, doc_text, doc_source)  # Streaming response
            print("\n")  # Newline for readability
        else:
            print("\n🚫 No relevant document found.\n")
