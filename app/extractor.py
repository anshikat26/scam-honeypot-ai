import re

UPI_PROVIDER_MAP = {
    "ybl": "PhonePe / Yes Bank",
    "okaxis": "Axis Bank",
    "axis": "Axis Bank",
    "okhdfcbank": "HDFC Bank",
    "oksbi": "State Bank of India",
    "paytm": "Paytm",
    "upi": "Generic UPI",
    "okicici": "ICICI Bank"
}

def extract_upi_ids(text: str):
    pattern = r"[a-zA-Z0-9.\-_]{2,}@[a-zA-Z]{2,}"
    matches = re.findall(pattern, text)

    results = []
    for upi in matches:
        handle = upi.split("@")[-1].lower()
        provider = UPI_PROVIDER_MAP.get(handle, "Unknown Provider")
        results.append({
            "upi_id": upi,
            "provider": provider
        })
    return results


def extract_bank_accounts(text: str):
    return re.findall(r"\b\d{9,18}\b", text)


def extract_links(text: str):
    return re.findall(r"https?://[^\s]+", text)
