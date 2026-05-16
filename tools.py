from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from datetime import datetime
import wikipedia

@tool
def search_tool(query: str) -> str:
    """Search the web for information about a topic."""
    search = DuckDuckGoSearchRun()
    return search.run(query)

@tool
def wiki_tool(query: str) -> str:
    """Search Wikipedia for information about a topic."""
    try:
        return wikipedia.summary(query, sentences=3)
    except Exception as e:
        return f"Wikipedia search failed: {str(e)}"

@tool
def save_tool(data: str) -> str:
    """Saves research data to a text file. Input must be a plain string."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"
    with open("research_output.txt", "a", encoding="utf-8") as f:
        f.write(formatted_text)
    return f"Data successfully saved to research_output.txt"