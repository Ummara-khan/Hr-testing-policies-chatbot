import streamlit as st
import requests

API_URL = "http://127.0.0.1:6000/query"

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="HR Policy Assistant",
    page_icon="🏢",
    layout="wide"
)

# -------------------------
# CSS (PRO UI)
# -------------------------
st.markdown("""
<style>

/* MAIN TITLE */
.title {
    font-size: 26px;
    font-weight: 600;
    text-align: center;
    margin-bottom: 10px;
}

/* CHAT CONTAINER */
.chat-box {
    max-width: 850px;
    margin: auto;
}

/* USER */
.user {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white;
    padding: 12px 16px;
    border-radius: 16px;
    margin: 8px 0;
    max-width: 75%;
    margin-left: auto;
}

/* BOT */
.bot {
    background: #f3f4f6;
    color: #111;
    padding: 12px 16px;
    border-radius: 16px;
    margin: 8px 0;
    max-width: 75%;
    margin-right: auto;
}

/* SIDEBAR STYLE */
.sidebar-title {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 10px;
}

.small-text {
    font-size: 13px;
    color: #666;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# SIDEBAR (HR INFO PANEL)
# -------------------------
with st.sidebar:

    st.markdown("### 🏢 HR Policy Assistant")

    st.markdown("""
    This assistant helps employees understand:
    
    - Leave policies
    - Attendance rules
    - Salary guidelines
    - Company SOPs
    - HR FAQs
    """)

    st.divider()

    st.markdown("### 📁 Upload HR Files")

    uploaded_files = st.file_uploader(
        "Upload policy documents (PDF/TXT)",
        accept_multiple_files=True
    )

    if uploaded_files:
        st.success(f"{len(uploaded_files)} file(s) selected")

    st.divider()

    st.markdown("### ⚙️ System Info")
    st.markdown("Model: Cloudflare Llama 3")
    st.markdown("RAG: ChromaDB Enabled")
    st.markdown("Status: 🟢 Active")

# -------------------------
# TITLE
# -------------------------
st.markdown("<div class='title'>🤖 HR Policy Chat Assistant</div>", unsafe_allow_html=True)

# -------------------------
# SESSION STATE
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# CHAT HISTORY
# -------------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot'>{msg['content']}</div>", unsafe_allow_html=True)

# -------------------------
# INPUT
# -------------------------
user_input = st.chat_input("Ask HR policy question...")

if user_input:

    # show user
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f"<div class='user'>{user_input}</div>", unsafe_allow_html=True)

    # call backend
    try:
        res = requests.post(API_URL, json={"question": user_input})
        data = res.json()

        bot_reply = data.get("answer", "No response")

        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        st.markdown(f"<div class='bot'>{bot_reply}</div>", unsafe_allow_html=True)

    except Exception as e:
        err = f"Error: {e}"
        st.session_state.messages.append({"role": "assistant", "content": err})
        st.markdown(f"<div class='bot'>{err}</div>", unsafe_allow_html=True)
