from fastapi import APIRouter
from app.model import RequestState
from agents.ai_agents import get_response_from_ai_agent

router = APIRouter()

ALLOWED_MODELS_NAMES = ["llama-3.1-8b-instant", "deepseek/deepseek-r1-0528:free"]

@router.post("/chat")
def chat_endpoint(request: RequestState):
    if request.model_name not in ALLOWED_MODELS_NAMES:
        return {"error": "Invalid model name"}
    
    response = get_response_from_ai_agent(llm_id=request.model_name, query=request.messages, allow_search=request.allow_search, system_prompt=request.system_prompt, provider=request.model_provider)

    return response 
