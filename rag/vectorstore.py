
from langchain_community.vectorstores import Chroma
from rag.embeddings import get_embeddings
import os

PERSIST_DIR = os.path.join(os.path.dirname(__file__), "chroma")

_vectorstore = None


def get_vectorstore():
    global _vectorstore

    if _vectorstore is None:
        _vectorstore = Chroma(
            persist_directory=PERSIST_DIR,
            embedding_function=get_embeddings()
        )

    return _vectorstore
