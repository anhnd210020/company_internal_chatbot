# session_manager.py

"""
Session manager module for handling multi-turn, fragmented user queries.

Responsibilities:
- Manage per-session text buffers.
- Accumulate message fragments into a full question.
- Track last update time per session.
- Store generated answers per session after background processing.
"""

import time
from typing import Dict, Optional
import uuid

class SessionState:
    """Store temporary state for a single conversation session."""
    def __init__(self) -> None:
        self.buffer: str = ""
        self.last_update: float = 0.0
        self.answer: Optional[str] = None
        self.current_question_id: Optional[str] = None
        self.history: list[dict] = []        

class SessionManager:
    """
    Manage user sessions:
    - Merge fragmented messages into one full question.
    - Track last update time to decide when to answer.
    """
    def __init__(self, compose_window: float = 10.0) -> None:
        # compose_window: number of seconds of "silence" required before considering the question complete
        self.sessions: Dict[str, SessionState] = {}
        self.compose_window = compose_window

    def _get_or_create_state(self, session_id: str) -> SessionState:
        state = self.sessions.get(session_id)
        if state is None:
            state = SessionState()
            self.sessions[session_id] = state
        return state
    
    def add_fragment(self, session_id: str, fragment: str) -> str:
        """
        Add a new question fragment into the session buffer.
        Returns the full accumulated question for that session.
        """
        now = time.time()
        state = self._get_or_create_state(session_id)

        fragment = fragment.strip()

        if not state.buffer:
            state.current_question_id = str(uuid.uuid4())

        if state.buffer:
            state.buffer += " " + fragment
        else:
            state.buffer = fragment

        state.last_update = now
        # reset previous answer if user is typing something new
        state.answer = None
        return state.buffer

    def get_state(self, session_id: str) -> Optional[SessionState]:
        """Return the raw session state (or None if not exists)."""
        return self.sessions.get(session_id)
    
    def pop_buffer(self, session_id: str) -> tuple[str, Optional[str]]:
        """
        Get the full question buffer and reset it.
        Returns (full_question, question_id).
        """
        state = self.sessions.get(session_id)
        if state is None:
            return "", None

        full_question = state.buffer.strip()
        qid = state.current_question_id

        state.buffer = ""
        state.last_update = 0.0
        state.current_question_id = None  # reset for next question

        return full_question, qid

    
    def set_answer(self, session_id: str, answer: str) -> None:
        """
        Store the generated answer for this session.
        """
        state = self._get_or_create_state(session_id)
        state.answer = answer

    def pop_answer(self, session_id: str) -> Optional[str]:
        """
        Get and clear the stored answer for this session.
        """
        state = self.sessions.get(session_id)
        if state is None:
            return None
        ans = state.answer
        state.answer = None
        return ans    
    
# Create a shared instance for the entire app
session_manager = SessionManager(compose_window=10.0)
