from fastapi import FastAPI
from core.intent import classify_intent
from core.admin_parser import parse_admin_command
from core.admin_handler import handle_admin_action
from core.rag import answer_product_question
from core.session import session

app = FastAPI()

@app.get("/")
def health():
    return {"status": "AI SERVICE RUNNING"}

@app.post("/ai/chat")
def chat(payload: dict):
    message = payload.get("message", "").strip()
    intent = classify_intent(message).intent

    if intent == "PRODUCT_QUERY":

        if session.last_product:
            keywords = ["battery", "camera", "price", "display", "performance", "features"]
            for k in keywords:
                if k in message.lower():
                    message = f"What is the {k} of {session.last_product}"
                    break

        reply = answer_product_question(message)

        known_products = ["Samsung Galaxy S24", "iPhone"]
        for p in known_products:
            if p.lower() in message.lower():
                session.last_product = p

        session.last_intent = intent

        return {
            "intent": intent,
            "reply": reply
        }

    if intent == "ADMIN_COMMAND":
        action = parse_admin_command(message)
        result = handle_admin_action(action)
        return {
            "intent": intent,
            "action": action,
            "result": result
        }

    return {
        "intent": intent,
        "reply": "I can help with shop products and inventory-related questions."
    }
