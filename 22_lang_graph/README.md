# Chapter 22 – LangGraph

Stateful graphs with nodes and conditional edges. Optional MongoDB checkpointer for conversation state.

## Requirements

- **OpenAI API key** in `.env` as `OPENAI_API_KEY`
- **MongoDB** (only for `chat_checkpoint.py`) – set connection in the script or env.

## Run

- **Basic / conditional graphs:**  
  `python chat_llm.py`  
  `python chat_llm_conditional.py`  
  `python chat_llm_conditional_with_logic.py`

- **With checkpoint (MongoDB):**  
  Ensure MongoDB is running and configured in `chat_checkpoint.py`, then:  
  `python chat_checkpoint.py`

## Files

- `chat.py`, `chat_llm.py` – Simple graph (e.g. single chatbot node).
- `chat_llm_conditional.py`, `chat_llm_conditional_with_logic.py` – Conditional edges (e.g. route to “chatbot_updated” or “endnode”).
- `chat_checkpoint.py` – Same graph with MongoDB checkpointer for persistent state.
- `test.py` – Extra tests or experiments.
