from fastapi import FastAPI
from core.intent import classify_intent
from core.rag import answer_product_question

app = FastAPI()

@app.get("/")
def health():
    return {"status": "AI SERVICE RUNNING"}


@app.post("/ai/intent")
def detect_intent(payload: dict):
    message = payload.get("message", "")
    intent = classify_intent(message)
    return intent.model_dump()



@app.post("/ai/chat")
def chat(payload: dict):
    message = payload.get("message", "")
    intent = classify_intent(message).intent

    if intent == "PRODUCT_QUERY":
        reply = answer_product_question(message)
        return {"intent": intent, "reply": reply}

    return {"intent": intent, "reply": "Not a product query."}
