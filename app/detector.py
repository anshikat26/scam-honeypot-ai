INTENT_KEYWORDS = {
    "threat": [
        "blocked", "suspended", "disabled", "deactivated",
        "closed", "paused", "terminated"
    ],
    "urgency": [
        "urgent", "immediately", "now", "today",
        "final", "last", "avoid", "before"
    ],
    "payment": [
        "pay", "payment", "charge", "fee", "amount",
        "deposit", "transfer", "send", "money"
    ],
    "action": [
        "click", "visit", "open", "verify",
        "update", "complete"
    ]
}

def detect_scam(text: str):
    text = text.lower()

    scores = {
        "threat": 0,
        "urgency": 0,
        "payment": 0,
        "action": 0
    }

    for intent, words in INTENT_KEYWORDS.items():
        for w in words:
            if w in text:
                scores[intent] += 1

    confidence = (
        scores["threat"] * 20 +
        scores["urgency"] * 15 +
        scores["payment"] * 30 +
        scores["action"] * 15
    )
    confidence = min(confidence, 100)

    if scores["payment"] > 0:
        return {
            "is_scam": True,
            "risk_level": "HIGH",
            "confidence": max(confidence, 80),
            "keywords_found": sum(scores.values())
        }

    if confidence >= 60:
        return {
            "is_scam": True,
            "risk_level": "HIGH",
            "confidence": confidence,
            "keywords_found": sum(scores.values())
        }

    if confidence >= 30:
        return {
            "is_scam": True,
            "risk_level": "MEDIUM",
            "confidence": confidence,
            "keywords_found": sum(scores.values())
        }

    return {
        "is_scam": False,
        "risk_level": "LOW",
        "confidence": confidence,
        "keywords_found": sum(scores.values())
    }
