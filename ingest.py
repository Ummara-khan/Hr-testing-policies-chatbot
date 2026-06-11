from uuid import uuid4
from rag import get_vectorstore
from utils import load_document, chunk_text

def ingest_file(path: str):
    text = load_document(path)
    chunks = chunk_text(text)

    db = get_vectorstore()

    db.add_texts(
        texts=chunks,
        ids=[str(uuid4()) for _ in chunks],
        metadatas=[{"source": path}] * len(chunks)
    )

    db.persist()

    return len(chunks)