from fastapi import FastAPI
from app.routes.upload import router as upload_router

app = FastAPI(
    title="Enterprise AI Research Assistant",
    version="1.0.0"
)

app.include_router(upload_router)