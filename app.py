from fastapi import FastAPI
from core.intent import classify_intent
from core.rag import answer_product_question
from core.admin import parse_admin_command

app = FastAPI()

@app.get("/")
def health():
    return {"status": "AI SERVICE RUNNING"}

@app.post("/ai/chat")
def chat(payload: dict):
    message = payload.get("message", "")
    intent = classify_intent(message).intent

    if intent == "PRODUCT_QUERY":
        return {
            "intent": intent,
            "reply": answer_product_question(message)
        }

    if intent == "ADMIN_COMMAND":
        return {
            "intent": intent,
            "action": parse_admin_command(message)
        }

    return {
        "intent": intent,
        "reply": "Unsupported request"
    }
