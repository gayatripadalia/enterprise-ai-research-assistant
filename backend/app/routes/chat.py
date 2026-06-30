from fastapi import APIRouter
from pydantic import BaseModel

import app.utils.document_store as document_store
from app.utils.ai_analyzer import answer_question

router = APIRouter()


class ChatRequest(BaseModel):
    document_id: int
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):

    document = document_store.get_document_by_id(
        request.document_id
    )

    if not document:
        return {
            "error": "Document not found."
        }

    answer = answer_question(
        document["extracted_text"],
        request.question
    )

    return {
        "document_id": document["id"],
        "filename": document["filename"],
        "question": request.question,
        "answer": answer
    }