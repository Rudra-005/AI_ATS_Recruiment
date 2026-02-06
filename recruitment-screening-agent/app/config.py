import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    USE_GROQ = os.getenv("USE_GROQ", "false").lower() == "true"
    
    OPENAI_MODEL = "gpt-3.5-turbo"
    GROQ_MODEL = "llama-3.3-70b-versatile"
    
    EMBEDDING_MODEL = "text-embedding-ada-002"
    MAX_TOKENS = 2000
    TEMPERATURE = 0.1
    FAISS_INDEX_PATH = "faiss_index.bin"
    DEMO_MODE = os.getenv("DEMO_MODE", "false").lower() == "true"