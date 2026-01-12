import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

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
SALES_SUMMARY
GENERAL_CHAT
UNKNOWN

If the message asks to list, show, display, or view all products
(e.g., "what are the products", "products in the database", "list products"),
return LIST_PRODUCTS.

If the message asks about total earning, profit, revenue, or income
by selling all products (optionally with a discount),
return SALES_SUMMARY.

Message: {message}

Return only the intent.
"""
    res = llm.invoke(prompt)
    return res.content.strip()
