from fastapi import FastAPI
from pydantic import BaseModel

from load_folder import load_all_files
from rag_engine import rag_query

app = FastAPI(title="RAG System (Auto Folder Loader)")

# -------------------------
# REQUEST MODEL
# -------------------------
class QueryRequest(BaseModel):
    question: str


# -------------------------
# STARTUP EVENT
# -------------------------
@app.on_event("startup")
def startup_event():
    result = load_all_files()
    print("=== DATA INGESTION COMPLETE ===")
    print(result)


# -------------------------
# QUERY ENDPOINT
# -------------------------
@app.post("/query")
async def query(req: QueryRequest):
    answer = rag_query(req.question)

    if isinstance(answer, dict):
        answer = (
            answer.get("response")
            or answer.get("message", {}).get("content")
            or str(answer)
        )

    return {
        "question": req.question,
        "answer": answer
    }