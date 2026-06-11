import requests
from config import GROQ_API_KEY, GROQ_API_URL, GROQ_MODEL

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def ask_llm(messages):
    try:
        # ---------------------------
        # FORCE VALID FORMAT
        # ---------------------------
        if isinstance(messages, str):
            messages = [
                {"role": "user", "content": messages}
            ]

        if isinstance(messages, dict):
            messages = [messages]

        payload = {
            "model": GROQ_MODEL,
            "messages": messages,
            "temperature": 0.2
        }

        response = requests.post(
            GROQ_API_URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        print("STATUS:", response.status_code)
        print("RAW:", response.text)

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"LLM Error: {str(e)}"
