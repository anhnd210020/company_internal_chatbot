# api.py

"""
API module for the Company Handbook Chatbot.
Handles:
- FastAPI application setup
- Request/response model definitions
- Chatbot query endpoint that interacts with the RAG pipeline
"""

from fastapi import FastAPI
from pydantic import BaseModel
from rag_core import generate_answer
from conversation_logger import log_interaction

app = FastAPI(title="Company Handbook Chatbot")


class ChatRequest(BaseModel):
    """Request body containing the user's question."""
    question: str

class ChatResponse(BaseModel):
    """Response body containing the chatbot's answer."""
    answer: str

@app.post("/chatbot_query", response_model=ChatResponse)
def chatbot_query(req: ChatRequest) -> ChatResponse:
    """
    Handle chatbot queries.

    This endpoint receives a question from the user,
    passes it to the RAG pipeline, and returns a structured response.
    """
    result = generate_answer(req.question)
    answer = result["answer"]

    # Log each question and answer
    log_interaction(req.question, answer)
    
    # Wrap the result into the Pydantic response model to ensure consistency.
    return ChatResponse(
        answer=result["answer"]
    )


