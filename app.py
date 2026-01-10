from fastapi import FastAPI
from core.intent import classify_intent
from core.admin_parser import parse_admin_command
from core.admin_handler import handle_admin_action
from core.rag import answer_product_question

app = FastAPI()

@app.get("/")
def health():
    return {"status": "AI SERVICE RUNNING"}

@app.post("/ai/chat")
def chat(payload: dict):
    message = payload.get("message", "").strip()
    intent = classify_intent(message).intent

    if intent == "PRODUCT_QUERY":
        return {"intent": intent, "reply": answer_product_question(message)}
    if intent == "ADMIN_COMMAND":
        action = parse_admin_command(message)
        result = handle_admin_action(action)
        return {"intent": intent, "action": action, "result": result}

    return {"intent": intent, "reply": "Unsupported request"}
