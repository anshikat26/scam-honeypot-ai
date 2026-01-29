import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

# ===============================
# App init
# ===============================
app = FastAPI(title="Agentic Scam Honeypot")

# ===============================
# CORS (important for UI)
# ===============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===============================
# Paths
# ===============================
BASE_DIR = os.path.dirname(os.path.abspath(_file_))
UI_DIR = os.path.join(BASE_DIR, "ui")

# ===============================
# Serve UI
# ===============================
if os.path.exists(UI_DIR):
    app.mount("/ui", StaticFiles(directory=UI_DIR), name="ui")

    @app.get("/", response_class=HTMLResponse)
    async def serve_ui():
        with open(os.path.join(UI_DIR, "index.html"), "r", encoding="utf-8") as f:
            return f.read()
else:
    @app.get("/")
    async def no_ui():
        return {"status": "UI folder not found"}

# ===============================
# Health check (for Render & judges)
# ===============================
@app.get("/health")
async def health():
    return {
        "status": "Agentic Scam Honeypot AI is running",
        "message": "Service is live and healthy"
    }

# ===============================
# MAIN BACKEND ENDPOINT (UI calls this)
# ===============================
@app.post("/engage")
async def engage_honeypot(request: Request):
    try:
        data = await request.json()
    except Exception:
        data = {}

    return {
        "status": "success",
        "agent": "honeypot",
        "analysis": "Scammer interaction simulated",
        "received_message": data
    }

# ===============================
# Fallback for wrong routes
# ===============================
@app.exception_handler(404)
async def not_found(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={"error": "Endpoint not found"}
    )
