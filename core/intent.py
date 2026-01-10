import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel
from typing import Literal
import json

load_dotenv()


class IntentResponse(BaseModel):
    intent: Literal[
        "PRODUCT_QUERY",
        "SALES_ANALYTICS",
        "INVENTORY_UPDATE",
        "UNKNOWN"
    ]

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

with open("prompts/intent.txt", "r", encoding="utf-8") as f:
    template_text = f.read()

prompt = PromptTemplate(
    template=template_text,
    input_variables=["message"]
)


def classify_intent(message: str) -> IntentResponse:
    chain = prompt | llm
    raw = chain.invoke({"message": message}).content

    try:
        data = json.loads(raw)
        return IntentResponse(**data)
    except Exception:
        return IntentResponse(intent="UNKNOWN")
