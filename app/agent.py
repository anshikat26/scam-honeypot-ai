def agent_reply(analysis: dict, extracted: dict, step: int):

    if not analysis["is_scam"]:
        return "Thank you for the information. I will check and get back to you."

    if step == 1:
        return "My account is blocked? I am worried. Can you please explain the issue?"

    if step == 2:
        if extracted["upi_ids"]:
            return "I tried paying but it failed. Can you confirm the UPI ID once?"
        if extracted["bank_accounts"]:
            return "Before transferring, I need to verify the bank account details."
        return "I am checking my details right now. Please stay connected."

    if step >= 3:
        return "I am facing some issues from my side. Please guide me step by step."

    return "Please tell me how to proceed."
