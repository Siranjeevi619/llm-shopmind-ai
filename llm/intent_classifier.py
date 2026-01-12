import os, config
from langchain_groq import ChatGroq

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model=os.getenv("GROQ_MODEL") or "llama-3.1-8b-instant",
    temperature=0
)

def classify_intent(message: str) -> str:
    prompt = f"""
Classify intent strictly.

Allowed:
ADD_PRODUCT
ADD_STOCK
SET_STOCK
GET_STOCK
REMOVE_PRODUCT
PRODUCT_INFO
LIST_PRODUCTS
SALES_QUERY
SALES_PREDICTION
GENERAL_CHAT
UNKNOWN

Message: {message}

Return only the intent.
"""
    res = llm.invoke(prompt)
    return res.content.strip()
