from load_folder import load_all_files
from rag_engine import rag_query

def chat():
    print("\n🚀 Initializing RAG System...\n")

    # ⚡ IMPORTANT FIX:
    # Only load once per run (you can later add a DB check to skip indexing)
    try:
        load_all_files()
    except Exception as e:
        print(f"⚠️ Indexing skipped/failed: {e}")

    print("\n🤖 RAG Chat Ready! Type 'exit' to quit.\n")

    while True:
        try:
            q = input("You: ").strip()

            if not q:
                continue

            if q.lower() in ["exit", "quit"]:
                print("Goodbye 👋")
                break

            answer = rag_query(q)

            # ⚡ safe output handling (prevents crash like 'response' error)
            if isinstance(answer, dict):
                answer = (
                    answer.get("response")
                    or answer.get("message", {}).get("content")
                    or str(answer)
                )

            print("\nBot:", answer, "\n")

        except Exception as e:
            print(f"\n❌ Error: {e}\n")


if __name__ == "__main__":
    chat()