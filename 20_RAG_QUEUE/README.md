# Chapter 20 – RAG with Queue (FastAPI + RQ)

RAG exposed as an API; heavy work runs in background workers via Redis RQ.

## Requirements

- **Redis** running locally (default port 6379)
- **Qdrant** at `http://localhost:6333` with the `learning_rag` collection (build it from `19_RAG` first)
- **OpenAI API key** in `.env` as `OPENAI_API_KEY`

## Run

1. **Start Redis** (if not already running).

2. **Start the RQ worker (separate terminal):**  
   On Windows:
   ```bash
   rq worker default --worker-class rq.worker.SimpleWorker
   ```
   On Linux/macOS:
   ```bash
   rq worker default
   ```

3. **Start the API:**  
   `python main.py`  
   Server runs at `http://127.0.0.1:8080`.

4. **Use the API:**
   - `POST /chat?query=your question` – returns `{"status": "queued", "job_id": "..."}`.
   - `GET /job-status?job_id=...` – returns the RAG response when the job is done.

## Structure

- `main.py` – Runs FastAPI with uvicorn.
- `server.py` – Routes: `/`, `/chat`, `/job-status`.
- `client/rq_client.py` – Redis queue connection.
- `queues/worker.py` – RAG job: Qdrant search + OpenAI completion.
