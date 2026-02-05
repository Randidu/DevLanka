import os
import openai
from pydantic import BaseModel
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Configure API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class AIResponse(BaseModel):
    content: str
    status: str # "success" or "error"

def get_ai_client():
    if not OPENAI_API_KEY:
        return None
    return openai.AsyncOpenAI(api_key=OPENAI_API_KEY)

async def analyze_code(code: str, language: str, task: str = "debug") -> AIResponse:
    """
    Analyzes code using OpenAI GPT-4o or GPT-3.5.
    task can be 'debug', 'explain', or 'tutor'.
    """
    client = get_ai_client()
    
    if not client:
        return AIResponse(
            content="OpenAI API Key is missing. Please check your .env file.",
            status="error"
        )

    system_prompt = "You are a helpful expert coding assistant."
    user_prompt = ""

    if task == "debug":
        system_prompt = f"You are an expert {language} debugger. Find bugs and provide corrected code with brief explanations."
        user_prompt = f"Debug this {language} code:\n\n{code}"
    elif task == "explain":
        system_prompt = f"You are a helpful teacher. Explain {language} code safely and simply to a beginner."
        user_prompt = f"Explain this {language} code:\n\n{code}"
    elif task == "tutor":
         system_prompt = "You are a friendly and encouraging programming tutor for the DevLanka platform."
         user_prompt = f"Student Question: {code} (Context: {language})"
    else:
        user_prompt = f"Review this {language} code:\n\n{code}"

    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo", # or gpt-4o if available/affordable
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=500
        )
        content = response.choices[0].message.content
        return AIResponse(content=content, status="success")
    except Exception as e:
        return AIResponse(content=f"OpenAI Error: {str(e)}", status="error")

async def moderate_content(text: str) -> bool:
    """
    Returns True if content is safe, False if unsafe/spam.
    Uses OpenAI Moderation API.
    """
    client = get_ai_client()
    if not client:
        return True # Fail open if AI is not configured

    try:
        # Use OpenAI's dedicated moderation endpoint is cheaper & better
        mod_response = await client.moderations.create(input=text)
        results = mod_response.results[0]
        
        # If flagged, it's unsafe (return False)
        return not results.flagged
    except:
        return True # Default to safe on error
