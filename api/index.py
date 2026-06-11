from fastapi import FastAPI
from pydantic import BaseModel

from load_folder import load_all_files
from rag_engine import rag_query

app = FastAPI()

# -------------------------
# CACHE DATA (IMPORTANT for serverless)
# -------------------------
DATA_LOADED = False


def ensure_data_loaded():
    global DATA_LOADED
    if not DATA_LOADED:
        load_all_files()
        DATA_LOADED = True


# -------------------------
# REQUEST MODEL
# -------------------------
class QueryRequest(BaseModel):
    question: str


# -------------------------
# ROUTES
# -------------------------
@app.get("/")
def home():
    return {"message": "RAG API running on Vercel"}


@app.post("/query")
async def query(req: QueryRequest):
    ensure_data_loaded()  # lazy load instead of startup event

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