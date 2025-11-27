# conversation_logger.py

from datetime import datetime
from pathlib import Path
import json
from typing import Optional

# Log file path
LOG_PATH = Path("chat_logs.jsonl")


def log_interaction(question: str, answer: str, question_id: Optional[str] = None) -> None:
    """
    Record each question and answer into a JSON Lines file.
    Each line is an object: {timestamp, question_id, question, answer}
    """
    entry = {
        "timestamp": datetime.utcnow().isoformat(),  # UTC time
        "question_id": question_id,                
        "question": question,
        "answer": answer,
    }

    # Open the file in append mode, add 1 more line of JSON
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
