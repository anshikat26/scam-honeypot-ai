from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.routes import router
import os

app = FastAPI(
    title="Agentic Scam Honeypot",
    docs_url="/docs",
    redoc_url="/redoc"
)

# =====================
# CORS (Judges ke liye)
# =====================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================
# ROUTES
# =====================
app.include_router(router)

# =====================
# UI SERVE (IMPORTANT)
# =====================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_PATH = os.path.join(BASE_DIR, "ui")

app.mount("/ui", StaticFiles(directory=UI_PATH), name="ui")

# Root -> UI
@app.get("/")
def serve_ui():
    return FileResponse(os.path.join(UI_PATH, "index.html"))

# Health check (Render + Judges)
@app.get("/health")
def health():
    return {
        "status": "Agentic Scam Honeypot AI is running",
        "message": "Service is live and healthy"
    }