# TubeTalkAI

> **A Advanced RAG Based AI assistant that lets you chat with YouTube videos — powered by Gemini**

---

## 🚀 Overview

**TubeTalkAI** is an advanced **Command Line Interface (CLI) tool** that allows users to **interact with YouTube videos conversationally**.  
Simply paste a YouTube URL, and TubeTalkAI will:

- Fetch the transcript automatically
- Enable you to **chat with the content**, asking questions or clarifying concepts
- Provide **timestamped answers** linked to relevant video segments
- Generate **summaries**, insights, and highlights — all powered by **Google’s Gemini LLM** and advanced **RAG (Retrieval-Augmented Generation)** techniques.

---

## 🧩 Features

- 🎙️ **Chat with YouTube videos** — get instant, timestamped answers.
- 🧾 **Summarization Engine** — generate concise summaries of long videos.
- 🧠 **RAG with Query Rewriting Fan-Out Model** — improves retrieval precision.
- 🧮 **Hybrid Storage System**
  - **Neo4j** for structured **graph knowledge**
  - **Quadrant** for **vector-based semantic retrieval**
- 🧰 **CLI-first experience** — simple, fast, and developer-friendly.
- ⚙️ **Extensible architecture** built with modular Python design.
- 🔗 Powered by **LangChain**, **Gemini API**, and **custom loaders**.

---

## 🏗️ Project Structure

```
TubeTalkAI/
│
├── llm/
│   ├── chatbot_engine.py        # Handles conversation logic
│   ├── query_rewriter.py        # Rewrites and optimizes queries (Fan-Out RAG)
│   └── __init__.py
│
├── loaders/
│   ├── youtube_loader.py        # Fetches and processes YouTube transcripts
│   └── __init__.py
│
├── stores/
│   ├── graph_store.py           # Manages Neo4j graph database
│   ├── vector_store.py          # Manages Quadrant vector database
│   └── __init__.py
│
├── utils/
│   ├── config.py                # Configuration and environment setup
│   ├── helpers.py               # Utility functions
│   ├── main.py                  # CLI entry point
│   ├── prompts.py               # Prompt templates for LLMs
│   ├── requirements.txt         # Project dependencies
│   └── __init__.py
│
└── venv/                        # Virtual environment (ignored in Git)
```

---

## 🧠 Tech Stack

| Component           | Technology                                          |
| ------------------- | --------------------------------------------------- |
| **LLM Engine**      | Gemini                                              |
| **Knowledge Graph** | Neo4j                                               |
| **Vector Store**    | Quadrant                                            |
| **Frameworks**      | LangChain, RAG                                      |
| **Language**        | Python                                              |
| **Other Tools**     | API calls, Custom Loaders, Advanced Query Rewriting |

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/TubeTalkAI.git
cd TubeTalkAI

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # for macOS/Linux
venv\Scripts\activate     # for Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 💬 Usage

```bash
# Run TubeTalkAI
python utils/main.py
```

Then paste any YouTube video URL when prompted:

```
🔗 Enter YouTube URL: https://www.youtube.com/watch?v=abc123xyz
```

Now, chat with the video:

```
👤 You: What are the main points discussed at 10 minutes?
🤖 TubeTalkAI: Around 10:15, the speaker talks about AI models scaling laws...
```

Or generate a summary:

```
👤 You: Summarize this video.
🤖 TubeTalkAI: The video discusses the evolution of transformer architectures...
```

---

## 🧪 Example Queries

- “Explain what the speaker meant by _‘retrieval optimization’_.”
- “What are the key takeaways from this video?”
- “Show me timestamps where reinforcement learning is mentioned.”

---

## 📊 Architecture Diagram (Conceptual)

```
          ┌──────────────────────────────┐
          │         YouTube URL          │
          └──────────────┬───────────────┘
                         │
            Fetch + Transcribe via Loader
                         │
           ┌─────────────▼─────────────┐
           │     Vector + Graph DB     │
           │  (Quadrant + Neo4j)       │
           └─────────────┬─────────────┘
                         │
           ┌─────────────▼─────────────┐
           │       RAG Engine          │
           │ (Query Rewrite + Gemini)  │
           └─────────────┬─────────────┘
                         │
                  CLI Chat Interface
```

---

## 🧠 Future Enhancements

- 🌐 Add multi-video context support.
- 🗣️ Integrate speech-to-text for live videos.
- 💾 Enable persistent chat sessions with memory.
- 📱 Build a lightweight GUI version.

---

---

## 🧾 License

MIT License © 2025 [Arpit Kumar Singh]
