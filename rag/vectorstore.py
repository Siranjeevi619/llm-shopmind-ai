from langchain_community.vectorstores import Chroma
from rag.embeddings import get_embeddings

PERSIST_DIR = "vectorstore/chroma"

def get_vectorstore():
    return Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=get_embeddings()
    )
