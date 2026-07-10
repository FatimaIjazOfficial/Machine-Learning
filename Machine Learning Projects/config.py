import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
    MAX_CONTENT_LENGTH = 250 * 1024 * 1024  # 250 MB
    ALLOWED_EXTENSIONS = {
        "pdf",
        "txt",
    }
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    if GROQ_API_KEY is None:
        raise ValueError(
            "GROQ_API_KEY not found in your .env file."
        )
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    LLM_MODEL = "llama-3.1-8b-instant"
    TEMPERATURE = 0.3
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    SEARCH_K = 3
