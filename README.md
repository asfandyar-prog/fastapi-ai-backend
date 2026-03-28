<div align="center">

```
███████╗ █████╗ ███████╗████████╗ █████╗ ██████╗ ██╗
██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║
█████╗  ███████║███████╗   ██║   ███████║██████╔╝██║
██╔══╝  ██╔══██║╚════██║   ██║   ██╔══██║██╔═══╝ ██║
██║     ██║  ██║███████║   ██║   ██║  ██║██║     ██║
╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝
```

# ⚡ FastAPI AI Backend

**Production-grade REST API infrastructure for serving AI agents, RAG pipelines, and LLM-powered systems**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-005571?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agent_Orchestration-FF6B35?style=for-the-badge)](https://langchain-ai.github.io/langgraph/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)

*This repo is the backend spine of my full-stack AI engineer portfolio — connecting agentic systems to the real world through clean, async, deployable APIs.*

</div>

---

## 🧠 What This Repository Is

This is **not** a tutorial project. It is the production backend layer that bridges my AI research and agent engineering work with deployable, real-world applications.

Every agent I've built — from scratch ReAct systems to LangGraph multi-agent workflows to multi-source RAG pipelines — lives as a Jupyter notebook or Python script. This repo transforms those into **REST APIs** that any frontend (React, mobile, other services) can consume.

**The goal:** take AI from research to shipped product.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                             │
│                                                                 │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐        │
│   │  React UI   │    │  Mobile App │    │  3rd Party  │        │
│   │  (Vercel)   │    │             │    │   Service   │        │
│   └──────┬──────┘    └──────┬──────┘    └──────┬──────┘        │
└──────────┼────────────────┼──────────────────┼───────────────┘
           │                │                  │
           ▼                ▼                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                    FASTAPI BACKEND (This Repo)                  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                     app/main.py                          │  │
│  │              CORS │ Middleware │ Router Registry          │  │
│  └──────────────────────────────────────────────────────────┘  │
│                           │                                     │
│          ┌────────────────┼────────────────┐                   │
│          ▼                ▼                ▼                   │
│   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │
│   │POST /chat/  │  │POST /stream/│  │POST /upload/│          │
│   │Single-turn  │  │SSE Streaming│  │PDF Ingestion│          │
│   │  response   │  │  real-time  │  │  for RAG    │          │
│   └──────┬──────┘  └──────┬──────┘  └──────┬──────┘          │
│          └────────────────┼────────────────┘                   │
│                           ▼                                     │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                   app/agents/                            │  │
│  │         ReAct Agent │ LangGraph │ RAG Pipeline           │  │
│  └──────────────────────────────────────────────────────────┘  │
│                           │                                     │
└───────────────────────────┼─────────────────────────────────────┘
                            │
           ┌────────────────┼────────────────┐
           ▼                ▼                ▼
   ┌──────────────┐  ┌─────────────┐  ┌──────────────┐
   │  OpenAI API  │  │  Vector DB  │  │  File Store  │
   │   / Groq     │  │  (Chroma)   │  │  (uploads/)  │
   └──────────────┘  └─────────────┘  └──────────────┘
```

---

## 📁 Repository Structure

```
fastapi-ai-backend/
│
├── 📂 app/                          # Core application package
│   ├── __init__.py
│   ├── main.py                      # Entry point — app factory, middleware, routers
│   │
│   ├── 📂 routers/                  # API route handlers
│   │   ├── __init__.py
│   │   ├── chat.py                  # POST /chat/ — single-turn agent response
│   │   ├── stream.py                # POST /stream/ — SSE streaming response
│   │   └── upload.py                # POST /upload/ — file ingestion for RAG
│   │
│   ├── 📂 agents/                   # Agent logic (plug-in zone)
│   │   ├── __init__.py
│   │   └── react_agent.py           # ReAct / LangGraph agent interface
│   │
│   ├── 📂 models/                   # Pydantic schemas
│   │   ├── __init__.py
│   │   └── schemas.py               # Request/Response data models
│   │
│   └── 📂 core/                     # Configuration
│       ├── __init__.py
│       └── config.py                # Settings, env variable management
│
├── 📂 tests/                        # Test suite
│   └── test_chat.py
│
├── 📂 uploads/                      # Runtime file storage (gitignored)
│
├── .env.example                     # Environment variable template
├── .gitignore
├── Dockerfile                       # Container definition
├── requirements.txt
└── README.md
```

---

## 🚀 API Endpoints

| Method | Endpoint | Description | Status |
|--------|----------|-------------|--------|
| `GET` | `/` | Health check — confirms backend is live | ✅ Live |
| `POST` | `/chat/` | Send a message, receive full agent response | 🔧 Building |
| `POST` | `/stream/` | Send a message, receive token-by-token SSE stream | 🔧 Building |
| `POST` | `/upload/` | Upload PDF/file for RAG pipeline ingestion | 🔧 Building |

### Request / Response Examples

**POST `/chat/`**
```json
// Request
{
  "message": "What are the key principles of quantum entanglement?",
  "session_id": "user_abc_123",
  "history": [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi! How can I help?"}
  ]
}

// Response
{
  "response": "Quantum entanglement refers to...",
  "session_id": "user_abc_123"
}
```

**POST `/stream/`** — Returns `text/event-stream`
```
data: Quantum
data: entanglement
data: refers
data: to...
```

**POST `/upload/`**
```json
// Response
{
  "filename": "quantum_computing_intro.pdf",
  "status": "success",
  "message": "quantum_computing_intro.pdf uploaded and ready for processing."
}
```

---

## ⚙️ Local Setup

```bash
# 1. Clone
git clone https://github.com/asfandyar-prog/fastapi-ai-backend.git
cd fastapi-ai-backend

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set environment variables
cp .env.example .env
# Open .env and fill in your API keys

# 5. Run the server
uvicorn app.main:app --reload

# 6. Open interactive docs
# http://localhost:8000/docs      ← Swagger UI
# http://localhost:8000/redoc     ← ReDoc
```

---

## 🐳 Docker

```bash
# Build
docker build -t fastapi-ai-backend .

# Run
docker run -p 8000:8000 --env-file .env fastapi-ai-backend
```

---

## 🔗 Agent Integration Map

This repo is designed to plug in agents from my other repositories:

```
AGENT SOURCE REPOS                    THIS REPO (entry point)
─────────────────────────────────────────────────────────────

framework-free-agent          ──────► app/agents/react_agent.py
(ReAct from scratch)                  └── /chat/ endpoint

agentic-systems-with-langgraph ─────► app/agents/react_agent.py
(LangGraph workflows)                 └── /stream/ endpoint

quantum-insight-rag           ──────► app/agents/react_agent.py
(Multi-source RAG)                    └── /upload/ + /chat/ endpoints
```

| Connected Repo | Role in This Backend |
|----------------|---------------------|
| [framework-free-agent](https://github.com/asfandyar-prog/framework-free-agent) | Core ReAct agent — `/chat/` endpoint |
| [agentic-systems-with-langgraph](https://github.com/asfandyar-prog/agentic-systems-with-langgraph) | LangGraph multi-agent — `/stream/` endpoint |
| [quantum-insight-rag](https://github.com/asfandyar-prog/quantum-insight-rag) | RAG pipeline — `/upload/` + `/chat/` endpoints |

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **API Framework** | FastAPI 0.110+ | Async REST API, auto Swagger docs |
| **Data Validation** | Pydantic v2 | Request/response schemas, type safety |
| **Agent Orchestration** | LangGraph | Multi-agent workflows, memory, reflection |
| **LLM Interface** | LangChain | LLM abstraction, tool calling |
| **Streaming** | Server-Sent Events (SSE) | Real-time token streaming to frontend |
| **Configuration** | pydantic-settings | Env variable management |
| **Containerization** | Docker | Reproducible deployment |
| **Deployment** | Railway / Render | Cloud hosting (free tier) |
| **Frontend** | React + Vercel | Chat UI (separate repo — coming soon) |

---

## 📈 Development Roadmap

- [x] Project structure and package layout
- [x] FastAPI app factory with CORS and middleware
- [x] Pydantic request/response schemas
- [x] Router architecture (`/chat`, `/stream`, `/upload`)
- [x] Dockerfile for containerization
- [ ] Connect ReAct agent to `/chat/` endpoint
- [ ] Implement SSE streaming via `/stream/`
- [ ] Integrate RAG pipeline with `/upload/`
- [ ] JWT authentication middleware
- [ ] Deploy to Railway
- [ ] React frontend (separate repo)
- [ ] Connect frontend to this backend (full-stack live demo)

---

## 🧪 Running Tests

```bash
pytest tests/
```

---

## 👤 Author

**Asfand Yar** — AI Engineer | BSc Computer Science, University of Debrecen (2027)

Specializing in Generative AI, Agentic Systems, and LLM Infrastructure.
Co-Lead @ Google Developer Groups Debrecen | VP @ International Students' Union

[![GitHub](https://img.shields.io/badge/GitHub-asfandyar--prog-181717?style=flat&logo=github)](https://github.com/asfandyar-prog)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Asfand_Yar-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/asfand-yar-3966b8291)
[![Email](https://img.shields.io/badge/Email-yarasfand886@gmail.com-EA4335?style=flat&logo=gmail)](mailto:yarasfand886@gmail.com)

---

<div align="center">

*Part of a full-stack AI engineering portfolio — research → agents → APIs → deployed products.*

</div>