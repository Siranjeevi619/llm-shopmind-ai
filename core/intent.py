import re
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

INTENT_KEYWORDS = [
    "received",
    "added",
    "stock",
    "inventory",
    "set",
    "available",
    "sold",
    "remaining",
    "units",
    "quantity"
]

def keyword_admin_detect(message: str) -> bool:
    msg = message.lower()
    return any(word in msg for word in INTENT_KEYWORDS)


with open("prompts/intent.txt", "r", encoding="utf-8") as f:
    prompt_text = f.read()

prompt = PromptTemplate(
    template=prompt_text,
    input_variables=["message"]
)


class IntentResult:
    def __init__(self, intent: str):
        self.intent = intent


def classify_intent(message: str) -> IntentResult:
    message = message.strip()

    # 🔥 HARD OVERRIDE (CRITICAL)
    if keyword_admin_detect(message):
        return IntentResult("ADMIN_COMMAND")

    # 🧠 LLM fallback
    chain = prompt | llm
    result = chain.invoke({"message": message})

    intent = result.content.strip().upper()

    if intent not in ["PRODUCT_QUERY", "ADMIN_COMMAND", "GENERAL_CHAT"]:
        intent = "GENERAL_CHAT"

    return IntentResult(intent)
