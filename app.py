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

    session.last_message = message

    if intent == "PRODUCT_QUERY":

        follow_up_keywords = [
            "battery", "camera", "price",
            "display", "performance", "features"
        ]

        if session.last_product:
            for kw in follow_up_keywords:
                if kw in message.lower():
                    message = f"What is the {kw} feature of {session.last_product}"
                    break

        reply = answer_product_question(message)

        # 🚨 SMART HUMAN FALLBACK
        if reply.lower() == "i don't know":
            return {
                "intent": intent,
                "reply": (
                    "I don’t have information about that because this assistant "
                    "is designed specifically for our shop.\n\n"
                    "Currently, we deal with products like smartphones and related accessories. "
                    "If you’d like details about any product we sell, I’ll be happy to help."
                )
            }

        # Update memory if product detected
        known_products = [
            "Samsung Galaxy S24",
            "iPhone"
        ]

        for product in known_products:
            if product.lower() in message.lower():
                session.last_product = product

        session.last_intent = intent

        return {
            "intent": intent,
            "reply": reply
        }

    # ---------------- ADMIN COMMAND ----------------
    if intent == "ADMIN_COMMAND":
        action = parse_admin_command(message)
        result = handle_admin_action(action)

        session.last_intent = intent

        return {
            "intent": intent,
            "action": action,
            "result": result
        }

    # ---------------- GENERAL CHAT ----------------
    return {
        "intent": intent,
        "reply": (
            "I’m here to help with our shop — including product details, "
            "availability, and inventory-related questions.\n\n"
            "Tell me what you’re looking for!"
        )
    }
