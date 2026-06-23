from fastapi import APIRouter
from pydantic import BaseModel

import app.utils.document_store as document_store
from app.utils.ai_analyzer import answer_question

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):

    if not document_store.DOCUMENT_TEXT:
        return {
            "error": "No document uploaded yet."
        }

    answer = answer_question(
        document_store.DOCUMENT_TEXT,
        request.question
    )

    return {
        "question": request.question,
        "answer": answer
    }