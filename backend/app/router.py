import logging
from typing import Dict, List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from model.huggingface import HuggingFaceInference

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()
model = HuggingFaceInference()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Dict[str, str]]


@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        logger.info(f"Received chat request with messages: {request.messages}")
        response = model.chat(request.messages)
        logger.info(f"Model response: {response}")
        return {"response": response}
    except Exception as e:
        logger.error(f"Error processing chat request: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
