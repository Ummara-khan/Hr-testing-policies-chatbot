import os

# Local folders (unchanged)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
DB_DIR = os.path.join(BASE_DIR, "chroma_db")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(DB_DIR, exist_ok=True)

# ------------------------
# GROQ CONFIG (NEW)
# ------------------------

GROQ_API_KEY = "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"  # safer than hardcoding

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Best fast model for RAG
GROQ_MODEL = "llama-3.1-8b-instant"