# ingest_handbook.py

"""
Ingestion script for the TTS Handbook.

This script:
- Walks through the pages/ directory
- Reads markdown files and converts them to plain text
- Chunks the text into smaller passages
- Encodes them using the embedding model
- Stores the results in a ChromaDB collection
"""

import os
import uuid
from typing import List

import markdown
from bs4 import BeautifulSoup

from config import PAGES_DIR, collection, embedding_model


def read_markdown_file(path: str) -> str:
    """
    Read a .md file and convert it to plain text.

    The markdown content is first rendered to HTML, then stripped to text.
    """
    with open(path, "r", encoding="utf-8") as file:
        md_content = file.read()

    html = markdown.markdown(md_content)
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator="\n")
    return text


def simple_chunk_text(text: str, max_chars: int = 1200) -> List[str]:
    """
    Simple text chunking by paragraphs with a character limit.

    This function:
    - Splits the input text into paragraphs
    - Merges paragraphs into chunks until max_chars is reached
    - Returns a list of text chunks

    Note:
        max_chars ≈ 200–300 tokens, which is suitable for RAG.
    """
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    chunks: List[str] = []
    current = ""

    for paragraph in paragraphs:
        if len(current) + len(paragraph) + 1 <= max_chars:
            current += ("\n" + paragraph) if current else paragraph
        else:
            if current:
                chunks.append(current)
            current = paragraph

    if current:
        chunks.append(current)

    return chunks


def ingest_pages() -> None:
    """
    Ingest all markdown files under PAGES_DIR into the Chroma collection.

    Steps:
        1. Walk through PAGES_DIR and find all .md files.
        2. Read and chunk each file into smaller passages.
        3. Encode each passage using the embedding model.
        4. Store ids, documents, metadata, and embeddings in ChromaDB.
    """
    all_texts: List[str] = []
    all_metadatas: List[dict] = []
    all_ids: List[str] = []

    for root, _, files in os.walk(PAGES_DIR):
        for fname in files:
            if not fname.endswith(".md"):
                continue

            file_path = os.path.join(root, fname)
            rel_path = os.path.relpath(file_path, PAGES_DIR)

            print(f"Processing file: {rel_path}")

            text = read_markdown_file(file_path)
            chunks = simple_chunk_text(text)

            for chunk in chunks:
                doc_id = str(uuid.uuid4())
                metadata = {
                    "source_file": rel_path,
                    "title": fname.replace(".md", ""),
                    "section": os.path.dirname(rel_path) or "root",
                }
                all_ids.append(doc_id)
                all_texts.append(chunk)
                all_metadatas.append(metadata)

    print(f"Total chunks to ingest: {len(all_texts)}")
    print("Encoding embeddings with intfloat/multilingual-e5-small...")

    # Recommended for E5 models:
    # Documents should be prefixed with "passage: "
    doc_inputs = [f"passage: {text}" for text in all_texts]

    embeddings = embedding_model.encode(
        doc_inputs,
        show_progress_bar=True,
        convert_to_numpy=True,
    ).tolist()

    print("Saving embeddings and documents to ChromaDB...")
    collection.add(
        ids=all_ids,
        documents=all_texts,
        metadatas=all_metadatas,
        embeddings=embeddings,
    )

    print("Ingestion completed.")


if __name__ == "__main__":
    ingest_pages()







