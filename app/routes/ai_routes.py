from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.services.ai_service import analyze_code

router = APIRouter()

class CodeRequest(BaseModel):
    code: str
    language: str
    task: str = "debug"  # 'debug' | 'explain'

class ChatRequest(BaseModel):
    message: str
    context: str = ""

@router.post("/analyze")
async def analyze_code_endpoint(request: CodeRequest):
    """
    Endpoint for the AI Code Assistant in the Editor.
    """
    if not request.code.strip():
        raise HTTPException(status_code=400, detail="Code cannot be empty")
        
    response = await analyze_code(request.code, request.language, request.task)
    return response

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """
    Endpoint for the AI Tutor Chatbot.
    """
    # Re-using analyze_code for now, but treating it as a 'tutor' task
    response = await analyze_code(request.message, "General Programming", task="tutor")
    return response
