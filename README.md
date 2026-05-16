# AI Research Agent

An AI-powered research assistant that searches the web, queries Wikipedia, and generates structured research summaries using LangGraph and Groq's LLaMA model.

## Features

- Web search using DuckDuckGo
- Wikipedia lookup
- Saves research output to a text file
- Structured JSON output using Pydantic
- Powered by Groq's free API (no cost!)

## Tech Stack

- Python 3.11
- [LangChain](https://langchain.com/)
- [LangGraph](https://langchain-ai.github.io/langgraph/)
- [Groq API](https://console.groq.com/) (llama-3.3-70b-versatile)
- DuckDuckGo Search
- Wikipedia

## Project Structure

```
AI_agent/
├── main.py              # Main agent logic
├── tools.py             # Tool definitions (search, wiki, save)
├── requirements.txt     # Dependencies
├── .env                 # API keys (not pushed to GitHub)
└── research_output.txt  # Generated research outputs
```

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/Shreyaaaaaak/AI_agent.git
cd AI_agent
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get your free API key at [console.groq.com](https://console.groq.com)

### 5. Run the agent
```bash
python main.py
```

## Usage (for example)

```
What can I help you research? Generative AI
```

The agent will search the web and Wikipedia, then return a structured response like:

```json
{
  "topic": "Generative AI",
  "summary": "Generative AI refers to...",
  "sources": ["Wikipedia", "DuckDuckGo"],
  "tools_used": ["search_tool", "wiki_tool"]
}
```
------------------------------------------------------------------
