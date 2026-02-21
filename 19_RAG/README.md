# Chapter 19 – RAG (Retrieval-Augmented Generation)

RAG over your own PDF using Qdrant and OpenAI.

## Requirements

- **Qdrant** running at `http://localhost:6333`
- **OpenAI API key** in `.env` as `OPENAI_API_KEY`

## Setup

1. Put your PDF in this folder (e.g. `git.pdf`) or set the path in `index.py`.
2. Create and activate a venv, then: `pip install -r ../requirements.txt` (or from repo root).
3. Add `OPENAI_API_KEY` to `.env` in the project root.

## Run

1. **Build the index (one-time):**  
   `python index.py`  
   This loads the PDF, splits it, embeds with OpenAI, and creates the Qdrant collection `learning_rag`.

2. **Chat:**  
   `python chat.py`  
   Enter queries; answers are based on retrieved chunks and include page numbers.

## Files

- `index.py` – Builds the vector index from PDF.
- `chat.py` – Interactive RAG chat using the existing collection.
