from fastapi import FastAPI
from core.intent import classify_intent
from core.admin import parse_admin_command
from core.rag import answer_product_question
from core.admin_handler import handle_admin_action

app = FastAPI()


@app.get("/")
def health():
    return {"status": "AI SERVICE RUNNING"}


@app.post("/ai/intent")
def detect_intent(payload: dict):
    message = payload.get("message", "").strip()
    intent = classify_intent(message)
    return {"intent": intent.intent}


@app.post("/ai/chat")
def chat(payload: dict):
    message = payload.get("message", "").strip()
    intent = classify_intent(message).intent
    if intent == "PRODUCT_QUERY":
        reply = answer_product_question(message)
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
        "reply": "Unsupported request"
    }
