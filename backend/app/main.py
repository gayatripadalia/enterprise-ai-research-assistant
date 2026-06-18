from fastapi import FastAPI, UploadFile, File
from app.utils.file_parser import extract_text

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_location = f"uploads/{file.filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    file_ext = file.filename.split(".")[-1]

    text = extract_text(file_location, file_ext)

    return {
        "filename": file.filename,
        "extracted_text_preview": text[:1000]
    }