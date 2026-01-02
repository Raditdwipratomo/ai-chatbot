from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from app.config import GROQ_API_KEY, OPENAI_API_KEY


def get_llm(provider, model):
    if provider == "Groq":
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY NOT FOUND")
        return ChatGroq(model=model, api_key=GROQ_API_KEY)
    elif provider == "Deepseek":
        if not OPENAI_API_KEY:
            raise ValueError("NOT FOUND")
        return ChatOpenAI(
    model="deepseek/deepseek-r1-0528:free",
    openai_api_key= OPENAI_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1"
)
    else:
        raise ValueError(f"Unknown provider: {provider}")