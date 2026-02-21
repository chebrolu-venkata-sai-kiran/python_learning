# Agentic AI – Learning Project

A structured learning repository covering **Python fundamentals** through **LLMs, RAG, agents, voice, and MCP**. All code and theory are organized by chapter so you can follow the progression from basics to agentic AI.

---

## Overview

- **Purpose:** Track daily learning and experiments in Python and AI/agent development.
- **Scope:** Python (variables, syntax, OOP, async, Pydantic) → LLM intro → Prompting → First agents → RAG → Multimodal → LangGraph → Memory → Voice agents → MCP → Agent SDK.
- **Tech stack:** Python 3.x, OpenAI API, LangChain, LangGraph, Mem0, Qdrant, Neo4j, Redis/RQ, FastAPI, Streamlit, MCP, OpenAI Agents SDK.

---

## Prerequisites & Setup

- **Python:** 3.10+ recommended.
- **Environment:** Use a virtual environment (e.g. `python -m venv .venv` then activate).
- **Install dependencies:**
  ```bash
  pip install -r requirements.txt
  ```
- **Environment variables:** Create a `.env` in the project root with `OPENAI_API_KEY` (and any other keys used in chapters). Some chapters use Gemini; configure `base_url`/API key in the relevant files if needed.
- **Optional services** (used by specific chapters):
  - **Qdrant:** `http://localhost:6333` (RAG, memory).
  - **Redis:** For RQ in `20_RAG_QUEUE`.
  - **MongoDB:** For LangGraph checkpoint in `22_lang_graph`.
  - **Neo4j:** For graph memory in `24_graph_memory`; set `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD` in `.env`.

---

## Project Structure

```
Agentic AI/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── 00_python/                   # First steps
├── 01_Chapter/                  # Core Python (variables, types, syntax)
├── 03_conditionals/             # Conditionals (if/else, match)
├── 04_loops/                    # Loops (for, while, enumerate, zip, etc.)
├── 05_functions/                # Functions (params, scope, lambda, imports)
├── 06_cafe_bussiness/           # Import patterns (package example)
├── 07_comprehensions/           # List, set, dict comprehensions & generators
├── 08_generators/               # Generators (yield, send, yield from)
├── 09_decorators/               # Decorators (basics, logging, auth)
├── 10_oops/                     # OOP (classes, inheritance, MRO, static/class/property)
├── 11_execptions/               # Exceptions (try/except, custom, file handling)
├── 12_concurrency_and_parallelism.py/  # Threading, multiprocessing, GIL, locks, queues
├── 13_async/                    # Async/await, daemon, race conditions, deadlock
├── 14_pydantic/                 # Pydantic (models, validators, nested, serialization)
├── 15_intro_llm/                # LLM intro (tokenization, Gemini)
├── 16_prompting/                # Prompting (zero-shot, few-shot, CoT, persona)
├── 17_Prompting_techniques/     # Prompting theory (Alpaca, ChatML, INST)
├── 18_First_Agent/              # First agents (OpenAI, weather, app creation)
├── 19_RAG/                      # RAG (PDF index + chat with Qdrant)
├── 20_RAG_QUEUE/                # RAG with FastAPI + RQ workers
├── 21_image/                    # Multimodal (image + text with OpenAI)
├── 22_lang_graph/               # LangGraph (graphs, conditional edges, checkpoint)
├── 23_Memory_Agent/             # Mem0 + vector store (short/long-term memory)
├── 24_graph_memory/             # Mem0 + Neo4j graph + vector store
├── 25_voice_agents/             # Voice agent (STT, TTS, tools)
├── 26_MCP/                      # MCP server & clients (tools, Streamlit)
├── 27_Agent_SDK/                # OpenAI Agents SDK (agents, tools, web search)
├── cursorapp_creation/          # To-Do web app (HTML/CSS) – agent-generated
└── langchain/                   # LangChain (chat, LCEL, RAG, embeddings, agents, MCP)
```

---

## Folder-by-Folder Guide

### `00_python/`

- **Purpose:** Minimal first program.
- **Files:**
  - `helloworld.py` – Simple `print("hello")` script.

---

### `01_Chapter/`

- **Purpose:** Core Python – variables, types, mutability, and basic syntax.
- **Concepts:** Integers, strings (indexing, slicing, encode/decode), sets (mutable), `id()` and mutability (e.g. `chapter_01.py`, `chapter_mutable_immutable.py`).
- **Files:** `chapter_01.py` … `chapter_11.py`, `chapter_mutable_immutable.py` – each focuses on one topic (variables, arithmetic, strings, sets, etc.).

---

### `03_conditionals/`

- **Purpose:** Conditional logic.
- **Files:** `01_if.py` … `05_if.py` (if/else variants), `01_match.py` (match/case). Covers branching and pattern matching.

---

### `04_loops/`

- **Purpose:** Iteration and loop control.
- **Files:** `01_forloop.py`, `02_for.py`, `03_enumerate.py`, `04_zip.py`, `05_while.py`, `06_break_and_continue.py`, `07_for_else.py`, `08_walrus.py`, `09_dict_and_match_case.py`. Covers `for`, `while`, `enumerate`, `zip`, break/continue, for-else, walrus operator, and dict + match.

---

### `05_functions/`

- **Purpose:** Functions – structure, scope, parameters, return, recursion, lambda, built-ins, imports.
- **Files:** `01_duplication.py` … `15_import.py` – readability, reuse, scopes, `global`/`non_local`, input params, return types, recursion, lambda, built-in functions, and different import styles.

---

### `06_cafe_bussiness/`

- **Purpose:** Package and import in practice.
- **Files:**
  - `main.py` – Demonstrates `import recipes.flavours`, `from ... import`, and `import ... as`.
  - `recipes/flavours.py` – Defines drinks (e.g. `cold_coffee`, `matcha`, `espresso`) used by `main.py`.

---

### `07_comprehensions/`

- **Purpose:** Comprehensions and generator expressions.
- **Files:** `01_list_comprehensions.py`, `02_set_comprehensions.py`, `03_dictionaries.py`, `04_generators.py`. List, set, and dict comprehensions; generator expressions.

---

### `08_generators/`

- **Purpose:** Generator functions and protocol.
- **Files:** `01_basics.py`, `02_infinite_generators.py`, `03_send_generators.py`, `04_yield_from_and_close.py`. `yield`, infinite generators, `.send()`, `yield from`, and closing.

---

### `09_decorators/`

- **Purpose:** Decorators and real-world use.
- **Files:** `01_basics.py` (custom decorator with `functools.wraps`), `02_logging_decorator.py`, `03_auth_decorator.py`.

---

### `10_oops/`

- **Purpose:** Object-oriented Python.
- **Files:** `01_simple_class.py` … `11_property_decorators.py` – simple classes, namespaces, attribute shadowing, `__init__`, inheritance/composition, base classes, MRO, `@staticmethod`, `@classmethod`, `@property`.

---

### `11_execptions/`

- **Purpose:** Exception handling and custom exceptions.
- **Files:** `01_basic.py` … `08_file_handeling.py` – basic try/except, multiple and complex handlers, custom exception classes, and file handling with exceptions.

---

### `12_concurrency_and_parallelism.py/`

- **Purpose:** Concurrency and parallelism in Python.
- **Concepts:** Threading, multiprocessing, GIL, locks, queues, process value sharing.
- **Files:** `01_threading.py` … `12_process_value.py` – threads, processes, GIL, locks, downloads, queues, and process-safe value sharing.

---

### `13_async/`

- **Purpose:** Async I/O and concurrency pitfalls.
- **Files:** `01_async.py` … `10_dead_lock.py` – `async`/`await`, running async code, thread/process with async, daemon vs non-daemon, race conditions, and deadlock examples.

---

### `14_pydantic/`

- **Purpose:** Data validation and settings with Pydantic.
- **Structure:**
  - `01_basics/` – First model, field examples, validators, nested/self-referential models (`01_first_model.py` … `09_self_reference.py`).
  - `02_advanced/` – Advanced nested models.
  - `03_serialization/` – Serialization (e.g. `01_serialization.py`).

---

### `15_intro_llm/`

- **Purpose:** Introduction to LLMs and tokenization.
- **Files:**
  - `01_tokenization/01_encode_and_decode_tokenization.py` – tiktoken encode/decode (e.g. for GPT).
  - `02_gemini/01_gemini.py`, `02_gemini_openai.py` – Gemini usage (native and via OpenAI-compatible client).

---

### `16_prompting/`

- **Purpose:** Prompting techniques in code.
- **Files:** `01_prompt.py` (basic prompt with Gemini), `02_zero_shot_prompting.py`, `03_few_shot_prompting.py`, `04_few_shot_prompting_with_rules.py`, `05_few_shot_prompting_with_rules_with_format.py`, `06_chain_of_thought_prompting.py`, `07_auto_chain_of_thought_prompting.py`, `07_online_chain_of_thought_prompting.py`, `08_persona_based_prompting.py`, plus `test.py` / `test_connection.py`. Covers zero-shot, few-shot, rules, format, chain-of-thought, and persona.

---

### `17_Prompting_techniques/`

- **Purpose:** Theory and formats for prompting (no code).
- **Files:** `thoery.txt` (overview of techniques), `CHAT_ML.MD`, `Alpaca_prompt.md`. Documents Alpaca, ChatML, and INST-style prompting.

---

### `18_First_Agent/`

- **Purpose:** First agent-style flows with OpenAI (ReACT-style: plan, tool, output).
- **Files:**
  - `00_validate_openai_key.py` – Validates OpenAI API access (Responses API). Uses `OPENAI_API_KEY` from `.env`.
  - `01_weather_api.py` – Weather API helper.
  - `02_weather_agent.py` – Agent loop: user input → plan → optional tool (e.g. weather) → output (JSON steps).
  - `03_weather_agent_parsed.py` – Parsed/structured version of the agent.
  - `04_agent_for_creating_app.py` – Agent that can create an app (e.g. leads into `cursorapp_creation`).

---

### `19_RAG/`

- **Purpose:** RAG over your own documents (PDF) using Qdrant.
- **Concepts:** Load PDF → split (RecursiveCharacterTextSplitter) → embed (OpenAI) → store in Qdrant → similarity search → LLM answer with context.
- **Files:**
  - `index.py` – Loads PDF (`git.pdf`), splits, embeds, and builds Qdrant collection `learning_rag`.
  - `chat.py` – Reads query, retrieves chunks from Qdrant, builds context, and gets GPT response with page references. Requires Qdrant at `http://localhost:6333` and an existing `learning_rag` collection (run `index.py` first).

---

### `20_RAG_QUEUE/`

- **Purpose:** RAG as a queue-backed API (FastAPI + Redis RQ) so heavy work runs in workers.
- **Concepts:** Client sends query → FastAPI enqueues job → RQ worker runs RAG (Qdrant + OpenAI) → client polls job status for result. On Windows, run worker with: `rq worker default --worker-class rq.worker.SimpleWorker`.
- **Files:**
  - `main.py` – Runs FastAPI app with uvicorn (e.g. port 8080).
  - `server.py` – FastAPI routes: `GET /`, `POST /chat?query=...`, `GET /job-status?job_id=...`; enqueues to Redis.
  - `client/rq_client.py` – RQ queue connection.
  - `queues/worker.py` – RAG job: similarity search on Qdrant + OpenAI completion; returns assistant message.

---

### `21_image/`

- **Purpose:** Multimodal AI – image + text (vision).
- **Concept:** Send image URL + text prompt to OpenAI; model returns caption or answer.
- **Files:** `main.py` – Single request with `image_url` and text (e.g. “give me a caption for this image”) using `gpt-4.1-mini`.

---

### `22_lang_graph/`

- **Purpose:** LangGraph – stateful graphs with nodes and conditional edges.
- **Concepts:** `StateGraph`, `TypedDict` state, nodes (e.g. chatbot, evaluator), conditional edges, optional checkpointing (MongoDB) for conversation state.
- **Files:**
  - `chat.py`, `chat_llm.py` – Basic graph (e.g. single chatbot node).
  - `chat_llm_conditional.py`, `chat_llm_conditional_with_logic.py` – Conditional routing (e.g. after “chatbot”, route to “chatbot_updated” or “endnode”).
  - `chat_checkpoint.py` – Same graph with MongoDB checkpointer for persistence.
  - `test.py` – Tests or experiments.

---

### `23_Memory_Agent/`

- **Purpose:** Memory-augmented agent (short/long-term) using Mem0.
- **Concepts:** **Short-term:** session/task scope. **Long-term:** persistent user facts, preferences, past interactions. Mem0 handles embedding + vector store (Qdrant); you add/search memories and inject them into the LLM context.
- **Files:** `memory.py` – Mem0 config (OpenAI embedder + LLM, Qdrant). Loop: user input → `mem_client.search(query, user_id="kiran")` → format memories → system prompt with context → LLM reply; can add memories for the user.

---

### `24_graph_memory/`

- **Purpose:** Memory with a graph store (Neo4j) in addition to vector (Qdrant) via Mem0.
- **Concept:** Same Mem0 pattern as `23_Memory_Agent`, but with `graph_store` (Neo4j) for relational/long-term structure alongside vector search.
- **Files:** `memory.py` – Config includes Neo4j + Qdrant; same conversational loop with search and LLM. **Env vars:** `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD` (and `OPENAI_API_KEY`).

---

### `25_voice_agents/`

- **Purpose:** Voice-based agent: speech-to-text, LLM + tools, text-to-speech.
- **Concepts:** STT (e.g. `speech_recognition`) → agent loop (plan, tools: weather, `run_command`) → TTS (OpenAI streaming audio with `LocalAudioPlayer`). Implements a “cursor-style” voice assistant with tools.
- **Files:**
  - `main.py` – Entry point for the voice flow.
  - `cursor.py` / `cursor_fixed.py` – Agent loop with tools (weather, run_command), JSON step format, and async TTS playback.

---

### `26_MCP/`

- **Purpose:** Model Context Protocol (MCP) – expose tools to LLM clients via a standard protocol.
- **Concepts:** MCP server exposes tools (e.g. Wikipedia, DuckDuckGo); clients (stdio or Streamlit) connect and use them in an agent.
- **Files:**
  - `mcp_server.py` – FastMCP server with `wikipedia_search` and `duckduckgo_search` (stdio transport).
  - `mcp_client.py` – MCP client (e.g. stdio).
  - `mcp_client_stdio.py` – Stdio-based client.
  - `resource_prompt_server.py` / `resource_prompt_client.py` – Resource/prompt MCP endpoints.
  - LangChain integration lives under `langchain/mcp/` (e.g. Streamlit agent using MCP tools).

---

### `27_Agent_SDK/`

- **Purpose:** OpenAI Agents SDK (`openai-agents` / `agents`) – high-level agents with tools.
- **Files:**
  - `hello.py` – Simple agent (name, instructions), no tools; `Runner.run_sync(agent, input="...")`.
  - `agent_with_websearch.py` – Same agent with `WebSearchTool()`.
  - `agent_with_function_as_tool.py` – Agent with custom function as tool.
  - `agents_as_tools.py` – Agents used as tools (composition).

---

### `cursorapp_creation/`

- **Purpose:** Simple To-Do web app (HTML/CSS) created as an agent output (from `18_First_Agent` style “create an app” flow).
- **Files:** `index.html` – To-Do UI (add task, list, delete). `style.css` – Styling. No backend; static front-end only.

---

### `langchain/`

- **Purpose:** LangChain and LangGraph examples – chat, prompts, LCEL, embeddings, RAG, images, agents, MCP.
- **Subfolders and main files:**
  - **Introduction:** `chat.py` (ChatOpenAI invoke), `streamlit.py`, `ollama.py` – basic chat and Streamlit/Ollama usage.
  - **LCEL:** `langchain.py` (prompt template + LLM, Streamlit travel guide), `regular_chain.py`, `simple_sequential_chain.py`, `blog_post_generator.py`, `marker_email_generator.py` – chains and pipelines.
  - **Prompt:** `prompt_template_demo.py`, `travel_guide.py`, `interview_tips.py` – prompt templates and use cases.
  - **chathistory:** `chat.py`, `chathistory.py`, `chathistory_streamlit.py` – chat with history (in-memory or Streamlit).
  - **embedings:** `demo.py`, `emebed_docs.py`, `similarity_search.py`, `job_search_embedings.py`, `job_search_embedings_FIASS.py` – embeddings and similarity search (incl. FAISS).
  - **rag:** `rag.py` (Chroma + retrieval chain), `rag_history.py`, `rag_history_pdf.py` – RAG with and without history, PDF.
  - **image:** `images_demo.py`, `images_demo_streamlit.py`, `kyc.py` – image inputs with LLM (e.g. KYC-style).
  - **agent:** `agent_demo.py`, `landmark_helper.py` – LangChain agents and tool helpers.
  - **mcp:** `mcp.py`, `mcp_server.py` – MCP server/client or adapter usage with LangChain.

---

## Implementation Theory (Summary)

| Area | Theory / Pattern |
|------|-------------------|
| **Python basics** | Variables, types, mutability (`id`), conditionals, loops, functions, comprehensions, generators, decorators, OOP, exceptions, threading/processes, async. |
| **Pydantic** | Declarative models, validators, nested/self-referential models, serialization. |
| **LLMs** | Tokenization (tiktoken), chat completion (OpenAI/Gemini), system/user messages. |
| **Prompting** | Zero-shot, few-shot, chain-of-thought, persona; Alpaca/ChatML/INST formats. |
| **Agents** | ReACT-style loop: plan → optional tool call → observe → output; JSON step format. |
| **RAG** | Load/split docs → embed → vector store (Qdrant/Chroma) → retrieve → LLM with context. |
| **Queue RAG** | API enqueues job; worker runs RAG; client polls for result (FastAPI + RQ). |
| **Multimodal** | `content`: text + `image_url` in one request. |
| **LangGraph** | State graph: nodes (e.g. chatbot), edges, conditional edges; optional checkpointer (MongoDB). |
| **Memory** | Mem0: embed + vector (and optionally graph) store; search by query/user_id; inject into system prompt. |
| **Voice** | STT → agent (tools) → LLM → TTS (streaming audio). |
| **MCP** | Server exposes tools; clients call them over stdio or HTTP; LangChain can wrap MCP as tools. |
| **Agent SDK** | Declarative agent (name, instructions, tools); `Runner.run_sync` / async for execution. |

---

## Applied Conventions

The following have been applied in this repo:

- **Naming:** Folders `03_conditionals` and `17_Prompting_techniques` (typos fixed). Root readme is `README.md`.
- **Secrets:** No hardcoded API keys or passwords. `18_First_Agent/00_validate_openai_key.py` uses `OPENAI_API_KEY` from `.env`; `24_graph_memory/memory.py` uses `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD` from env.
- **Per-chapter READMEs:** Added in `19_RAG`, `20_RAG_QUEUE`, `22_lang_graph`, `25_voice_agents`, `26_MCP`, and `cursorapp_creation` with run instructions and env vars.
- **.gitignore:** Root `.gitignore` includes `.env`, `venv/`, `.venv/`, `__pycache__/`, `.pyc`, and common IDE/OS patterns.
- **Code quality:** `result.metadata['page_label']` / `result.metadata['source']` spacing fixed in `19_RAG/chat.py` and `20_RAG_QUEUE/queues/worker.py`.

For Neo4j in `24_graph_memory`, set in `.env`: `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD`.

---

## Quick Reference – Run Commands

- **RAG index (19):** `python 19_RAG/index.py` (then run `chat.py`; needs Qdrant).
- **RAG queue (20):** Start Redis, run `rq worker default --worker-class rq.worker.SimpleWorker`, then `python 20_RAG_QUEUE/main.py`; call `POST /chat?query=...` and `GET /job-status?job_id=...`.
- **MCP server (26):** `python 26_MCP/mcp_server.py` (stdio); use MCP client or LangChain Streamlit app to call tools.
- **Voice agent (25):** Run `cursor_fixed.py` or `main.py` (mic + speakers required).
- **LangGraph (22):** Run the desired script (e.g. `chat_llm_conditional.py`); for checkpoint, ensure MongoDB is running and configured.

---

*This README describes the repository as of the last update. For the exact set of files in each folder, refer to the project tree above.*
