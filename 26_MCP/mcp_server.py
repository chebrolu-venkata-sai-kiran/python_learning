from typing import List
import wikipedia
from ddgs import DDGS
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Tool Server")

@mcp.tool()
def wikipedia_search(query: str) -> str:
    """Search Wikipedia for a summary of a topic."""
    try:
        # returns a string as hinted
        return wikipedia.summary(query, sentences=2)
    except Exception as e:
        return f"Error occurred while searching Wikipedia: {str(e)}"

@mcp.tool()
def duckduckgo_search(query: str) -> list[str]:
    """Search the web using DuckDuckGo and return a list of result snippets."""
    try:
        # DDGS() must be instantiated as a context manager
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=5)
            # Returns a list of strings to match list[str] hint
            return [r["body"] for r in results]
    except Exception as e:
        # Returns a list containing the error message to maintain type safety
        return [f"Error occurred while using DDGS: {str(e)}"]

if __name__ == "__main__":
    # Recommended: use host="0.0.0.0" if you need to access this from outside localhost
    #mcp.run(transport="streamable-http")
    mcp.run(transport="stdio")

