from fastapi import FastAPI

from app.routes.upload import router as upload_router
from app.routes.chat import router as chat_router

app = FastAPI(
    title="Enterprise AI Research Assistant",
    version="1.0.0"
)

app.include_router(upload_router)
app.include_router(chat_router)