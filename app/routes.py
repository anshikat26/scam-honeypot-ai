from fastapi import APIRouter, Header, HTTPException
from app.detector import detect_scam
from app.extractor import extract_upi_ids, extract_bank_accounts, extract_links
from app.agent import agent_reply

router = APIRouter()

SECRET_API_KEY = "12345"
SESSION_STORE = {}

@router.post("/honeypot")
def honeypot(payload: dict, x_api_key: str = Header(None)):

    if x_api_key != SECRET_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    text = payload.get("text", "")
    session_id = payload.get("session_id", "default")

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

    return {
        "is_scam": analysis["is_scam"],
        "risk_level": analysis["risk_level"],
        "confidence": analysis["confidence"],
        "keywords_found": analysis["keywords_found"],
        "agent_reply": reply,
        "extracted_data": extracted,
        "step": step
    }
