from fastapi import FastAPI
from core.intent import classify_intent
from core.admin_parser import parse_admin_command
from core.admin_handler import handle_admin_action
from core.rag import answer_product_question
from core.session import session
from core.shop_catalog import find_product
from core.fallback_chat import shop_fallback

app = FastAPI()

@app.get("/")
def health():
    return {"status": "AI SERVICE RUNNING"}

@app.post("/ai/chat")
def chat(payload: dict):
    message = payload.get("message", "").strip()
    intent = classify_intent(message).intent

    if intent == "ADMIN_COMMAND":
        action = parse_admin_command(message)
        result = handle_admin_action(action)
        session.add(message, result)
        return {"intent": intent, "result": result}

    product = find_product(message)
    if product:
        session.last_product = product

    if not product and session.last_product:
        short = ["battery", "camera", "price", "display", "features", "performance"]
        if any(k in message.lower() for k in short):
            message = f"{message} of {session.last_product}"
            product = session.last_product

    if product:
        reply = answer_product_question(message)
        if reply:
            session.add(message, reply)
            return {"intent": "PRODUCT_QUERY", "reply": reply}

    reply = shop_fallback(message, session.history)
    session.add(message, reply)
    return {"intent": intent, "reply": reply}
