<div align="center">

<img src="https://img.shields.io/badge/LangGraph-Multi--Agent-7F77DD?style=for-the-badge&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-Dashboard-009688?style=for-the-badge&logoColor=white" />
<img src="https://img.shields.io/badge/Groq-LLM-0F6E56?style=for-the-badge&logoColor=white" />
<img src="https://img.shields.io/badge/LangChain-Framework-993C1D?style=for-the-badge&logoColor=white" />
<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" />

<br/><br/>

```
  ╔═══════════════════════════════╗
  ║   🤖  C O D E R  B U D D Y   ║
  ║   AI Multi-Agent Dev Team     ║
  ╚═══════════════════════════════╝
```

### *Natural language in → working project out*

*A multi-agent AI development team that turns your request into a complete, working codebase — file by file — using real developer workflows, now managed via an interactive web dashboard.*

</div>

<div>
Coder Buddy Project/
├── .junie/                       # Junie agent related files
├── .vscode/                      # VS Code configurations
└── Coder Buddy Project/          # Main codebase
    ├── .env                      # API keys & Env variables
    ├── .venv/                    # Main python virtual environment (with all dependencies)
    ├── Projects/                 # Generated project workspaces
    ├── agent/                    # Code logic / Multi-agent structure
    │   ├── resources/            # Templates library & assets
    │   ├── ui/                   # Web Dashboard frontend assets (HTML, CSS, JS)
    │   └── ...                   
    ├── main.py                   # Main entry file (starts Web UI or CLI)
    ├── pyproject.toml            # Dependencies metadata
    └── README.md                 # Project documentation

</div>

---

## 🏗️ Architecture

Four specialized agents work in sequence, executing transition check loops and handing off structured context — like a real development team:

```
┌──────────────┐     ┌────────────────┐     ┌─────────────────┐     ┌──────────────────┐
│   🗂 Planner  │ ──▶ │  🏛 Architect  │ ──▶ │    💻 Coder     │ ──▶ │   🔍 Reviewer    │
│              │     │                │     │                 │     │                  │
│ Analyzes the │     │ Breaks plan    │     │ Writes files,   │     │ Compiles syntax, │
│ request and  │     │ into file-     │     │ runs tools,     │     │ runs unittests   │
│ generates a  │     │ level tasks    │     │ iterates with   │     │ and loops back   │
│ project plan │     │ with context   │     │ ReAct loop      │     │ if tests fail    │
└──────────────┘     └────────────────┘     └─────────────────┘     └──────────────────┘
       │                     │                       │                       │
    Pydantic              Pydantic             Tool Use Loop            Auto Runner
    Schema                Schema            (write · read · templates)  (unittest check)
```

---

## 🚀 Key Upgrades & Features

### 💻 1. Interactive Web Dashboard UI
- Running `python main.py` opens a browser dashboard at `http://localhost:8000/`.
- Features an input prompt card, a real-time progress pipeline timeline, and an auto-scrolling terminal log console showing backend stdout streams.

### 🔐 2. Production User Authentication Templates
- Pre-built code templates for **JWT token-based auth** (FastAPI) and **Session-based auth** (Flask).
- Fully responsive **Glassmorphic Login/Signup HTML UI templates** utilizing localized token storage.

### 🧪 3. Advanced Automated Testing in Reviewer Loop
- Automatic scan for unit test scripts (`test_*.py` or `tests/` directories).
- Execution of unit test suites (`python -m unittest`) within the review phase to guarantee correctness.

### 🐳 4. Cloud Hosting & Deployment Configs
- Containerization setup: **Dockerfile** and **docker-compose.yml** configuration for local and cloud environments.
- Platform blueprints: **Render** (`render.yaml`) and **Vercel** (`vercel.json`) configurations.
- Custom step-by-step guides (`DEPLOY.md`) automatically created for every project.

---

## 📂 Module Structure

```
agent/
├── config/       # Python · dotenv     → Env configuration & output paths
├── llm/          # Groq · Ollama       → LLM client initialization
├── models/       # Pydantic            → Validation schemas & agent states
├── prompts/      # LangChain           → Prompt templates per agent
├── resources/    # Templates Library   → Auth (FastAPI/Flask/UI), Docker, Vercel, Render configs
├── tools/        # Custom OS tools     → write_file · read_file · list_files · get_template
├── ui/           # Web Assets          → index.html, style.css, app.js
├── services/     # Micro-agent logic   → Node implementations & state routers
└── graph.py      # LangGraph           → Assembles, compiles & exposes the StateGraph
```

---

## 🏁 Getting Started

### Prerequisites

| Requirement | Notes |
|---|---|
| `uv` package manager | Install from [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/) |
| Groq API key | Create one at [console.groq.com/keys](https://console.groq.com/keys) |

### ⚙️ Installation & Running

```bash
# 1. Clone/navigate to directory and create/activate virtual environment
uv venv
# source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate           # Windows

# 2. Install dependencies
uv pip install -r pyproject.toml

# 3. Configure environment
cp .sample_env .env              # then fill in your values

# 4. Start Coder Buddy Web UI (Default)
uv run python main.py

# 5. Run in CLI terminal mode
uv run python main.py --cli
```

---

## 🧪 Example Prompts

Try these out of the box to test the auth, testing, and deployment features:

> 🔐 **Full-Stack Task Board with Auth & Docker**
> Create a comprehensive task board web app with a Python backend using FastAPI and SQLite. Include JWT authentication for registration and login, fully responsive HTML login page, unittest validation suite, and a Dockerfile for deployment.

> 📊 **Product Catalog with Session Auth**
> Build a product catalogue system using Flask sessions, SQLAlchemy db models, unit testing suites, and a render.yaml configuration guide.

---

## 🔧 Available Tools

| Tool | Description |
|---|---|
| `write_file` | Safely writes content to a path-validated file |
| `read_file` | Reads an existing file from the output project |
| `list_files` | Lists all files in a directory |
| `get_template` | Retrieves pre-defined templates for JWT Auth, Docker, Vercel, Render, or Unittest |

---

<div align="center">

<!-- Copyright © Codebasics Inc. All rights reserved. -->
📧 **Contact Me:** [pavansoni210129@gmail.com](mailto:pavansoni210129@gmail.com)
<br/><br/>
Thanks for visiting Coder Buddy!

</div>