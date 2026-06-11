from pypdf import PdfReader

def load_document(path: str) -> str:
    if path.endswith(".pdf"):
        reader = PdfReader(path)
        return "\n".join(p.extract_text() or "" for p in reader.pages)

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def chunk_text(text, size=500, overlap=80):
    chunks = []
    start = 0

    while start < len(text):
        chunks.append(text[start:start+size])
        start += size - overlap

    return chunks