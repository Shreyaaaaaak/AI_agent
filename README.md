# 🤖 AI Research Agent

> An autonomous research assistant that searches the web, queries Wikipedia, and delivers structured research summaries — powered by **LangGraph** + **Groq LLaMA 3.3-70B**.

![Python](https://img.shields.io/badge/Python-3.11-3670A0?style=flat-square&logo=python&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-0.2-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLaMA%203.3--70B-F55036?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## What it does

Give it any research topic and the agent autonomously:

1. **Searches the web** via DuckDuckGo for recent information
2. **Queries Wikipedia** for background knowledge
3. **Synthesizes both sources** using LLaMA 3.3-70B (via Groq's free API)
4. **Returns structured JSON output** with summary, sources, and tools used
5. **Saves results** to a local text file for later reference

```
$ python main.py

What can I help you research? > Generative AI

{
  "topic": "Generative AI",
  "summary": "Generative AI refers to algorithms that can create new content...",
  "sources": ["Wikipedia", "DuckDuckGo"],
  "tools_used": ["search_tool", "wiki_tool"]
}
```

---

## Architecture

```
User Input
    │
    ▼
┌─────────────────────────────────────┐
│           LangGraph Agent           │
│                                     │
│  ┌──────────┐    ┌───────────────┐  │
│  │ DuckDuck │    │   Wikipedia   │  │
│  │  Search  │    │    Lookup     │  │
│  └──────────┘    └───────────────┘  │
│         \              /            │
│          ▼            ▼             │
│     ┌──────────────────────┐        │
│     │  Groq LLaMA 3.3-70B  │        │
│     │   (Synthesis Layer)  │        │
│     └──────────────────────┘        │
└─────────────────────────────────────┘
    │
    ▼
Structured JSON + Saved Output File
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Agent framework | LangGraph 0.2 |
| LLM | Groq API — LLaMA 3.3-70B Versatile |
| Web search | DuckDuckGo Search (no API key needed) |
| Knowledge base | Wikipedia via `langchain-community` |
| Output schema | Pydantic v2 |
| Language | Python 3.11 |

---

## Project Structure

```
AI_agent/
├── main.py              # Agent graph definition and entry point
├── tools.py             # Tool definitions (search, wiki, save)
├── requirements.txt     # All dependencies
├── .env                 # API keys — NOT committed to GitHub
└── research_output.txt  # Generated research outputs
```

---

## Getting Started

### Prerequisites

- Python 3.11+
- A free Groq API key → [console.groq.com](https://console.groq.com)

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/Shreyaaaaaak/AI_agent.git
cd AI_agent

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Groq API key
echo "GROQ_API_KEY=your_key_here" > .env

# 5. Run the agent
python main.py
```

> **Note:** Groq's API is completely free for this use case — no credit card required.

---

## Example Output

**Input:** `"What is LangGraph?"`

```json
{
  "topic": "LangGraph",
  "summary": "LangGraph is a library for building stateful, multi-actor applications with LLMs. It extends LangChain by enabling cyclic computation graphs, making it ideal for agentic workflows where an LLM must reason, act, and observe in a loop.",
  "sources": ["Wikipedia", "DuckDuckGo"],
  "tools_used": ["search_tool", "wiki_tool", "save_tool"]
}
```

---

## Why LangGraph over vanilla LangChain?

LangGraph allows the agent to loop — it can decide to search again if the first result isn't sufficient, rather than executing tools in a fixed linear chain. This makes the research behavior genuinely agentic rather than scripted.

---

## Limitations & Future Improvements

- [ ] Add a Streamlit or Gradio web UI
- [ ] Support multi-turn conversations with memory
- [ ] Integrate arXiv search for academic topics
- [ ] Add citation formatting (APA / MLA)
- [ ] Deploy as a web API using FastAPI

---

## Built by

**Shreya Kaushik** — ECE @ KIIT University (2027)  
[GitHub](https://github.com/Shreyaaaaaak) · [LinkedIn](https://www.linkedin.com/in/shreyakaushik2308)

---

## License

MIT — feel free to fork and build on this.
