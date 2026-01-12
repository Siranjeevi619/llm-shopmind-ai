from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import llm.intent_classifier as ic
import llm.command_parser as cp
import core.router as router

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    role: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    try:
        intent = ic.classify_intent(req.message)
        payload = cp.parse_command(intent, req.message)

        payload["_raw_message"] = req.message

        result = router.route(intent, payload, req.role)
        return ChatResponse(response=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
