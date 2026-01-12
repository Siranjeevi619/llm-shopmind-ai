import os
import json
import re
from langchain_groq import ChatGroq
from core.sanitize import sanitize_keys
from dotenv import load_dotenv
from inventory.inventory_service import list_products

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model=os.getenv("GROQ_MODEL") or "llama-3.1-8b-instant",
    temperature=0
)

# ---------- deterministic helpers ----------

def extract_product_id(message: str):
    msg = message.lower()
    for p in list_products():
        pid = str(p["_id"]).lower()
        name = p["name"].lower()
        if pid in msg or name in msg:
            return p["_id"]
    return None


def extract_price_and_quantity(message: str):
    """
    Extract price and quantity deterministically.
    Examples:
      price 40000
      into 40000
      with 40 units
      stock 40
    """
    msg = message.lower()

    price = None
    quantity = None

    # price patterns
    price_match = re.search(r"(price|into|to)\s+(\d+)", msg)
    if price_match:
        price = int(price_match.group(2))

    # quantity / stock patterns
    qty_match = re.search(r"(\d+)\s*(units|unit|qty|quantity|stock)", msg)
    if qty_match:
        quantity = int(qty_match.group(1))

    return price, quantity

# ---------- main parser ----------

def parse_command(intent: str, message: str) -> dict:
    payload = {}

    # Always inject product_id deterministically
    pid = extract_product_id(message)
    if pid:
        payload["product_id"] = pid

    # Handle UPDATE_PRODUCT deterministically
    if intent == "UPDATE_PRODUCT":
        price, quantity = extract_price_and_quantity(message)

        if price is not None:
            payload["price"] = price
        if quantity is not None:
            payload["quantity"] = quantity

        return payload

    # ---- fallback to LLM for other intents ----
    prompt = f"""
Convert message to JSON.

Intent: {intent}
Message: {message}

Rules:
- Output ONLY valid JSON
- No explanation
- No markdown
- If unsure, return {{}}

Schemas:
ADD_PRODUCT -> {{"product_id": "...", "name": "...", "stock": number, "price": number}}
ADD_STOCK -> {{"quantity": number}}
SET_STOCK -> {{"quantity": number}}
GET_STOCK -> {{}}
REMOVE_PRODUCT -> {{}}
SALES_SUMMARY -> {{"discount_percent": number}}
GENERAL_CHAT -> {{}}
"""
    res = llm.invoke(prompt)
    raw = res.content.strip()

    if raw.startswith("{"):
        try:
            payload.update(json.loads(raw))
        except json.JSONDecodeError:
            pass

    return sanitize_keys(payload)
