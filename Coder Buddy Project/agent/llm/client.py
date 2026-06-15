import os
from langchain_groq.chat_models import ChatGroq
from langchain_ollama import ChatOllama
import agent.config  # Triggers dotenv loading and settings initialization

# Read model configuration from environment
ollama_model = os.getenv("OLLAMA_MODEL")

if ollama_model:
    # Use ChatOllama for local LLM
    llm = ChatOllama(
        model=ollama_model,
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        temperature=0
    )
else:
    # Use ChatGroq for cloud LLM API
    llm = ChatGroq(model="openai/gpt-oss-120b")
