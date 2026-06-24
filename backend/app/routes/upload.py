print("UPLOAD ROUTE LOADED ✔")
import os
import time
from fastapi import APIRouter, UploadFile, File

from app.utils.document_store import save_document

from app.utils.file_parser import extract_text
from app.utils.ai_analyzer import analyze_text
import app.utils.document_store as document_store


router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_location = os.path.join(
        UPLOAD_DIR,
        f"{int(time.time())}_{file.filename}"
    )

    with open(file_location, "wb") as f:
        f.write(await file.read())

    file_ext = file.filename.split(".")[-1]

    # STEP 1: extract text
    text = extract_text(file_location, file_ext)
    document_store.DOCUMENT_TEXT = text

    print("TEXT EXTRACTED ✔")
    # STEP 2: send to AI (Ollama / Llama)
    ai_result = analyze_text(text)

    save_document(
    file.filename,
    text,
    ai_result
)

    print("AI ANALYSIS DONE ✔")
    # STEP 3: return everything
    return {
        "filename": file.filename,
        "extracted_text_preview": text[:2000],
        "ai_summary": ai_result
    }
