# config.py

"""
Configuration module for the RAG system.
Handles:
- Loading environment variables
- Gemini client configuration
- Embedding model initialization
- ChromaDB vector store setup
"""

import os
from dotenv import load_dotenv
from google import genai
import chromadb
from sentence_transformers import SentenceTransformer

# Load environment variables
load_dotenv()

# Gemini configuration (LLM for text generation)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing. Please set it in the .env file.")

client = genai.Client(api_key=GEMINI_API_KEY)

# Gemini model used for text generation
GEN_MODEL = "gemini-2.5-flash"
JUDGE_MODEL = GEN_MODEL

# Embedding model configuration (Multilingual E5)
EMBEDDING_MODEL_NAME = "intfloat/multilingual-e5-small"
embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)

# Dataset paths
PAGES_DIR = "./pages"          # Directory containing markdown files
CHROMA_DIR = "./chroma_db"     # Directory for Chroma vector database

# ChromaDB client and collection setup
chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)

COLLECTION_NAME = "handbook_chunks"

collection = chroma_client.get_or_create_collection(
    name=COLLECTION_NAME,
    metadata={"description": "TTS Handbook markdown chunks processed with E5 embeddings"},
)
