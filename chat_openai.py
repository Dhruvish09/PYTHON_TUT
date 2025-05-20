from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import openai
import os

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    model: str = "gpt-3.5-turbo"

@app.post("/chat")
async def chat_with_openai(chat_request: ChatRequest):
    try:
        response = openai.ChatCompletion.create(
            model=chat_request.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": chat_request.message},
            ]
        )
        return {"reply": response['choices'][0]['message']['content'].strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
