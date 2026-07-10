from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from config import Config


def create_vector_store(documents):

    if not documents:
        return None

    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=Config.CHUNK_SIZE,
        chunk_overlap=Config.CHUNK_OVERLAP,
    )

    chunks = text_splitter.split_documents(documents)

    # Create embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name=Config.EMBEDDING_MODEL
    )

    # Create FAISS vector store
    vector_store = FAISS.from_documents(
        chunks,
        embeddings,
    )

    return vector_store
