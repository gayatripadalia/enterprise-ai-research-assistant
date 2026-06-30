from fastapi import APIRouter
import app.utils.document_store as document_store

router = APIRouter()


@router.get("/documents")
async def get_documents():

    documents = document_store.get_all_documents()

    return documents