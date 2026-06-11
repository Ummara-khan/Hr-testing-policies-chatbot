from rag import get_vectorstore
from llm import ask_llm

def rag_query(question: str, k: int = 4):
    db = get_vectorstore()

    docs = db.similarity_search(question, k=k)

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are a helpful assistant.

Use ONLY the context below to answer.

Context:
{context}

Question:
{question}

Answer clearly and simply:
"""

    return ask_llm(prompt)