def agent_reply(analysis: dict, extracted: dict, step: int):

    if not analysis.get("is_scam"):
        return "Thank you for the information."

    if extracted.get("links"):
        return "The link is not opening properly. Can you resend it?"

    if extracted.get("bank_accounts"):
        return "I will do the bank transfer. Please share the IFSC code."

    if extracted.get("upi_ids"):
        return (
            "I tried sending the money but it failed. "
            "Can you confirm the UPI ID or provide another one?"
        )

    if analysis.get("risk_level") == "HIGH":
        return "I want to resolve this urgently. Please guide me with the next step."

    if step == 1:
        return "My account is blocked? I am worried. Please help me."

    if step == 2:
        return "Okay, I understand. How do I complete the verification?"

    return "Please tell me what I should do next to fix this."
