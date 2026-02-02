from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from app.routes import router
import os

app = FastAPI(
    title="Agentic Scam Honeypot",
    description="AI-powered scam engagement honeypot",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.get("/")
def serve_ui():
    return FileResponse(os.path.join(BASE_DIR, "ui", "index.html"))

app.include_router(router)
