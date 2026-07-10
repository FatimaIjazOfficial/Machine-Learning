from rag.embeddings import create_vector_store
from rag.loaders import load_documents
from rag.qa_chain import create_qa_chain

# Global variables
vector_store = None
qa_chain = None


def process_documents():
    global vector_store
    global qa_chain

    print("Loading documents...")
    documents = load_documents()
    print("Documents loaded:", len(documents))
    if not documents:
        print("No documents found.")
        vector_store = None
        qa_chain = None
        return False

    print("Creating vector store...")
    vector_store = create_vector_store(documents)
    print("Vector store:", vector_store)
    if vector_store is None:
        print("Failed to create vector store.")
        qa_chain = None
        return False

    print("Creating QA chain...")
    qa_chain = create_qa_chain(vector_store)
    print("QA Chain:", qa_chain)
    if qa_chain is None:
        print("Failed to create QA chain.")
        return False

    print("Everything initialized successfully.")
    return True


def get_qa_chain():
    return qa_chain


def get_vector_store():
    return vector_store


def clear_rag():
    global vector_store
    global qa_chain
    vector_store = None
    qa_chain = None
