import os
from config import DATA_DIR
from ingest import ingest_file

def load_all_files():
    files = []

    for f in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, f)

        if os.path.isfile(path) and (path.endswith(".pdf") or path.endswith(".txt")):
            files.append(path)

    if not files:
        print("No files found in data folder")
        return

    total_chunks = 0

    for file in files:
        print(f"Indexing: {file}")
        chunks = ingest_file(file)
        total_chunks += chunks

    print(f"\nDONE → Files: {len(files)}, Chunks: {total_chunks}")