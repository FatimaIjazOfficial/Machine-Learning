import os
from langchain_community.document_loaders import PyPDFLoader,TextLoader
from config import Config


def load_documents():

    # Load all PDF and TXT files from the uploads folder.
    documents = []

    if not os.path.exists(Config.UPLOAD_FOLDER):
        return documents

    for filename in os.listdir(Config.UPLOAD_FOLDER):
        file_path = os.path.join(
            Config.UPLOAD_FOLDER,
            filename,
        )

        if not os.path.isfile(file_path):
            continue

        try:
            if filename.lower().endswith(".pdf"):
                loader = PyPDFLoader(file_path)
                documents.extend(loader.load())
            elif filename.lower().endswith(".txt"):
                loader = TextLoader(file_path)
                documents.extend(loader.load())
        except Exception as e:
            print(f"Error loading {filename}: {e}")

    return documents
