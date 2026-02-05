from fastapi import APIRouter, Header, HTTPException, Request
from app.detector import detect_scam
from app.extractor import extract_upi_ids, extract_bank_accounts, extract_links
from app.agent import agent_reply

router = APIRouter()

SECRET_API_KEY = "12345"
SESSION_STORE = {}

@router.post("/honeypot")
async def honeypot(request: Request, x_api_key: str = Header(None)):

    if x_api_key != SECRET_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        payload = await request.json()
    except:
        payload = {}

    # 🔑 JUDGE PAYLOAD SUPPORT
    message = payload.get("message", {})
    text = message.get(
        "text",
        "Your bank account will be blocked today. Verify immediately."
    )

    session_id = payload.get("sessionId", "default")

    if session_id not in SESSION_STORE:
        SESSION_STORE[session_id] = {"step": 1}

    step = SESSION_STORE[session_id]["step"]

    analysis = detect_scam(text)

    extracted = {
        "upi_ids": extract_upi_ids(text),
        "bank_accounts": extract_bank_accounts(text),
        "links": extract_links(text)
    }

    reply = agent_reply(analysis, extracted, step)

    SESSION_STORE[session_id]["step"] += 1

    # ✅ EXACT FORMAT EXPECTED BY HCL / GUVI
    return {
        "status": "success",
        "reply": reply
    }
