# rag_core.py

"""
Core RAG logic module.
Responsible for:
- Embedding user queries
- Retrieving relevant context from ChromaDB
- Constructing the final LLM prompt
- Generating the final answer using Gemini
"""

from typing import List, Dict

from config import collection, embedding_model, client, GEN_MODEL


def embed_query(text: str) -> List[float]:
    """
    Embed the user's query using the e5-multilingual model.

    According to the e5 model guidelines:
    - Query inputs should be prefixed with: "query: "
    """
    query_input = f"query: {text}"
    vector = embedding_model.encode([query_input], convert_to_numpy=True)[0]
    return vector.tolist()


def retrieve_context(question: str, top_k: int = 5) -> List[Dict]:
    """
    Retrieve the top_k most relevant chunks from the vector database.
    Returns a list of dictionaries containing:
    - text
    - metadata
    - similarity score
    """
    query_vector = embed_query(question)

    print("[DEBUG] Query vector dimension:", len(query_vector))
    print("[DEBUG] Retrieving top_k:", top_k)

    results = collection.query(
        query_embeddings=[query_vector],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    contexts = []
    docs = results["documents"][0]
    metas = results["metadatas"][0]
    dists = results["distances"][0]

    print("\n[DEBUG] Retrieved results:")
    for doc, meta, dist in zip(docs, metas, dists):
        print(f"- File: {meta.get('source_file')} | Score: {dist}")

    # Aggregate matched chunks into a structured list
    for doc, meta, dist in zip(docs, metas, dists):
        contexts.append(
            {
                "text": doc,
                "metadata": meta,
                "score": dist,
            }
        )

    print("[DEBUG] Retrieved context length:", sum(len(c["text"]) for c in contexts))
    return contexts


def build_prompt(question: str, contexts: List[Dict]) -> str:
    """
    Build the final prompt for the LLM.
    All retrieved context snippets are merged with separators.
    """
    context_text = "\n\n---\n\n".join(
        f"[Source: {c['metadata'].get('title', 'unknown')}]\n{c['text']}"
        for c in contexts
    )

    prompt = f"""
You are an internal company assistant referencing the official Handbook.
Your task is to answer clearly and concisely.

You MUST rely ONLY on the information provided in the CONTEXT below.

LANGUAGE RULES:
1. Detect the language of the user question.
2. If the user asks in English → answer in English.
3. If the user asks in Vietnamese → answer in Vietnamese.
4. If the answer cannot be found in context:
   - If the user asks in English → reply exactly:
     "I could not find the exact information in the internal documentation."
   - If the user asks in Vietnamese → reply exactly:
     "Tôi không tìm thấy thông tin chính xác trong tài liệu nội bộ."

CONTEXT:
{context_text}

USER QUESTION:
{question}

Answer in the same language as the user question:
"""
    return prompt

def generate_answer(question: str, top_k: int = 5) -> Dict:
    """
    Full RAG pipeline:
    1. Retrieve relevant context.
    2. Build the prompt.
    3. Generate an answer using Gemini.
    """
    contexts = retrieve_context(question, top_k=top_k)
    prompt = build_prompt(question, contexts)

    response = client.models.generate_content(
        model=GEN_MODEL,
        contents=prompt,
    )

    answer_text = response.text

    # Prepare the list of source metadata to return to the API
    sources = []
    for ctx in contexts:
        meta = ctx["metadata"]
        sources.append(
            {
                "title": meta.get("title"),
                "section": meta.get("section"),
                "source_file": meta.get("source_file"),
            }
        )

    return {
        "answer": answer_text,
        "sources": sources,
    }


if __name__ == "__main__":
    sample_question = "What is the leave policy for employees?"
    result = generate_answer(sample_question)
    print("Q:", sample_question)
    print("A:", result["answer"])
    print("Sources:", result["sources"])