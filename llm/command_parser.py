import os
import json
import config
from langchain_groq import ChatGroq
from core.sanitize import sanitize_keys

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model=os.getenv("GROQ_MODEL") or "llama-3.1-8b-instant",
    temperature=0
)

def parse_command(intent: str, message: str) -> dict:
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
ADD_STOCK -> {{"product_id": "...", "quantity": number}}
SET_STOCK -> {{"product_id": "...", "quantity": number}}
GET_STOCK -> {{"product_id": "..."}}
REMOVE_PRODUCT -> {{"product_id": "..."}}
GENERAL_CHAT -> {{}}
"""
    res = llm.invoke(prompt)
    raw = res.content.strip()

    if not raw or not raw.startswith("{"):
        return {}

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return {}

    return sanitize_keys(data)
