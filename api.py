# api.py

"""
API module for the Company Handbook Chatbot.
Handles:
- FastAPI application setup
- Request/response model definitions
- Chatbot query endpoint that interacts with the RAG pipeline
- Uses SessionManager for message accumulation (per user_id + chat_id)
- Uses BackgroundTasks to wait (10s) and generate answers without blocking requests
"""

import time
import asyncio
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

from rag_core import generate_answer
from conversation_logger import log_interaction
from session_manager import session_manager

app = FastAPI(title="Company Handbook Chatbot")

# ==== Request/Response models ====

class ChatRequest(BaseModel):
    """
    Request body containing the user's question fragment.
    - user_id: identifier of the user (employee id / email / etc.)
    - chat_id: identifier of a conversation belonging to that user
    - question: the fragment the user just sent
    """
    user_id: str
    chat_id: str
    question: str

class ChatResponse(BaseModel):
    """Response body containing the chatbot's answer or status message."""
    answer: str

# ==== Helper: build session_key from user_id + chat_id ====

def make_session_key(user_id: str, chat_id: str) -> str:
    """
    Combine user_id + chat_id into a unique key for SessionManager.
    Example: "user123:chatA"
    """
    return f"{user_id}:{chat_id}"

# ==== Background task ====

async def process_session_after_timeout(session_id: str, started_at: float) -> None:
    """
    Background task:
    - Wait compose_window seconds.
    - Check if there has been new input after 'started_at'.
    - If not, treat the buffer as a final question, call RAG, and store the answer.
    """
    await asyncio.sleep(session_manager.compose_window)

    state = session_manager.get_state(session_id)
    if state is None:
        return

    # If there's newer activity after this task was scheduled, do nothing.
    if state.last_update > started_at:
        # User continued typing after we scheduled this task => skip.
        return

    # Pop question buffer (final merged question + question_id)
    final_question, question_id = session_manager.pop_buffer(session_id)
    if not final_question:
        return

    # Call RAG pipeline
    history = state.history if hasattr(state, "history") else None
    result = generate_answer(final_question, history=history)
    answer = result["answer"]

    # Log Q&A
    log_interaction(final_question, answer, question_id=question_id)

    # History update: added 1 new question and answer
    state.history.append({
        "user": final_question,
        "assistant": answer,
    })
    # Keep up to 5 recent turns (can increase to 10)
    if len(state.history) > 5:
        state.history = state.history[-5:]

    # Store answer for later retrieval
    session_manager.set_answer(session_id, answer)

# ==== Endpoints ====

@app.post("/chatbot_query", response_model=ChatResponse)
async def chatbot_query(req: ChatRequest, background_tasks: BackgroundTasks) -> ChatResponse:
    """
    Receive a fragment of the user's question.

    Logic:
    - Compute session_key = user_id + chat_id.
    - Append the fragment to the corresponding session buffer.
    - Schedule a background task:
        - wait compose_window seconds,
        - if no new fragment arrives → treat it as a final question → call RAG → store answer.
    - Immediately return a status message WITHOUT blocking the client.
    """
    session_key = make_session_key(req.user_id, req.chat_id)

    # 1) Add fragment to buffer
    _ = session_manager.add_fragment(session_key, req.question)

    # 2) Schedule background task with the current timestamp
    started_at = time.time()
    background_tasks.add_task(process_session_after_timeout, session_key, started_at)

    # 3) Return immediately (do not wait for LLM)
    return ChatResponse(
        answer="(Waiting for you to finish your question... answer will be ready soon.)"
    )
    
@app.get("/chatbot_result/{user_id}/{chat_id}", response_model=ChatResponse)
async def get_chatbot_result(user_id: str, chat_id: str) -> ChatResponse:
    """
    Retrieve the final answer for a given user_id + chat_id.

    - If the answer is ready → return it and clear it from the session.
    - If no answer is ready yet → return a status message.
    """
    session_key = make_session_key(user_id, chat_id)
    ans = session_manager.pop_answer(session_key)

    if ans is None:
        return ChatResponse(
            answer="(Answer is not ready yet, or no complete question has been detected.)"
        )

    return ChatResponse(answer=ans)


