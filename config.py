import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# --- Neo4j Config ---
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# --- Google Gemini Config ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_API_URL = os.getenv("GOOGLE_API_URL")

# --- OpenAI Config ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# --- Default LLM ---
LLM_GPT = ChatOpenAI(temperature=0, model_name="gpt-4-turbo")

print("config.py loaded successfully with LLM_GPT.")
