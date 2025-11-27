# app_streamlit.py

"""
Streamlit frontend for the Company Handbook Chatbot.

This app:
- Manages a per-browser chat session using Streamlit session_state.
- Sends user questions to the FastAPI backend as fragments.
- Polls the backend until a final answer is available.
"""

import time
import uuid

import requests
import streamlit as st

# Change this if your FastAPI app is running on a different host/port.
API_BASE_URL = "http://localhost:8000"


def init_session_state() -> None:
    """Initialize Streamlit session state variables (only once)."""
    if "chat_id" not in st.session_state:
        # Each browser tab corresponds to a separate chat session.
        st.session_state.chat_id = str(uuid.uuid4())
    if "user_id" not in st.session_state:
        st.session_state.user_id = "demo_user"
    if "messages" not in st.session_state:
        # Store chat history as a list of messages:
        # [{"role": "user" | "assistant", "content": "..."}]
        st.session_state.messages = []


def call_chatbot_api(user_id: str, chat_id: str, question: str) -> str:
    """
    Send a question fragment to the FastAPI backend, then poll for the final answer.

    This uses:
      - POST /chatbot_query
      - GET  /chatbot_result/{user_id}/{chat_id}
    """
    payload = {
        "user_id": user_id,
        "chat_id": chat_id,
        "question": question,
    }

    # 1) Send fragment to /chatbot_query
    try:
        requests.post(
            f"{API_BASE_URL}/chatbot_query",
            json=payload,
            timeout=30,
        )
    except Exception as exc:  # noqa: BLE001
        return f"(Error calling backend: {exc})"

    # 2) Poll /chatbot_result until answer is ready
    waiting_msg = (
        "(Answer is not ready yet, or no complete question has been detected.)"
    )
    poll_interval = 1.0

    while True:
        try:
            resp = requests.get(
                f"{API_BASE_URL}/chatbot_result/{user_id}/{chat_id}",
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
        except Exception as exc:  # noqa: BLE001
            return f"(Error getting result from backend: {exc})"

        answer = data.get("answer", "")

        # If the backend says the answer is not ready yet → keep waiting
        if answer.strip() == waiting_msg:
            time.sleep(poll_interval)
            continue

        # When the backend returns a real answer → return it
        return answer


def main() -> None:
    """Run the Streamlit chat application."""
    st.set_page_config(
        page_title="Company Handbook Chatbot",
        page_icon="💬",
        layout="centered",
    )

    init_session_state()

    st.title("💬 Company Handbook Chatbot")
    st.caption(
        "Ask questions about TTS / company policies, HR, IT, tools, travel, and more."
    )

    # Top bar: user_id input + "New chat" button
    cols = st.columns([3, 1])
    with cols[0]:
        st.session_state.user_id = st.text_input(
            "User ID",
            value=st.session_state.user_id,
            help="Use an employee ID, email, or any stable identifier.",
        )
    with cols[1]:
        if st.button("New chat"):
            # Start a new conversation: reset chat_id and history.
            st.session_state.chat_id = str(uuid.uuid4())
            st.session_state.messages = []
            st.success("Started a new chat session.")

    st.write(f"**Chat ID:** `{st.session_state.chat_id}`")

    # Render full chat history from session_state
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input box
    user_input = st.chat_input("Type your question here...")
    if user_input:
        # 1) Append user message to history
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        # 2) Render user message immediately in the UI
        with st.chat_message("user"):
            st.markdown(user_input)

        # 3) Call backend and render assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = call_chatbot_api(
                    st.session_state.user_id,
                    st.session_state.chat_id,
                    user_input,
                )
                st.markdown(answer)

        # 4) Append assistant answer to history
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )


if __name__ == "__main__":
    main()
