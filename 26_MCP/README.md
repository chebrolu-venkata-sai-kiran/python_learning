# Chapter 26 – MCP (Model Context Protocol)

Expose tools (e.g. Wikipedia, DuckDuckGo) to LLM clients via the MCP protocol.

## Requirements

- Dependencies from root `requirements.txt` (includes `mcp`, `wikipedia`, `ddgs`, etc.)
- For Streamlit/LangChain client: `langchain-mcp-adapters`, LangChain env configured

## Run

1. **Start the MCP server (stdio):**  
   `python mcp_server.py`  
   Tools: `wikipedia_search(query)`, `duckduckgo_search(query)`.

2. **Use a client:**
   - `mcp_client.py` / `mcp_client_stdio.py` – Direct MCP client.
   - Or run the LangChain Streamlit app under `langchain/mcp/` that connects to this server (over HTTP use `transport="streamable-http"` and the matching URL).

## Files

- `mcp_server.py` – FastMCP server with Wikipedia and DuckDuckGo tools (stdio).
- `mcp_client.py`, `mcp_client_stdio.py` – MCP clients.
- `resource_prompt_server.py`, `resource_prompt_client.py` – Resource/prompt MCP endpoints.
