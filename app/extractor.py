import re

def extract_upi_ids(text: str):
    pattern = r"[a-zA-Z0-9.\-_]{2,}@[a-zA-Z]{2,}"
    return re.findall(pattern, text)

def extract_bank_accounts(text: str):
    return re.findall(r"\b\d{9,18}\b", text)

def extract_links(text: str):
    return re.findall(r"https?://[^\s]+", text)
