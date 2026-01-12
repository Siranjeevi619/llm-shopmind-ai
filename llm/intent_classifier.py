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
UPDATE_PRODUCT
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

Rules:
- If the message contains "update stock", "set stock", "change stock",
  "modify stock", or "adjust stock", return SET_STOCK.
- If the message asks about availability, quantity, or stock of a specific product
  (e.g., "how many iphone15 are available"), return GET_STOCK.
- If the message asks to list or show all products, return LIST_PRODUCTS.
- If the message asks about total earning, profit, revenue, or income
- If the message asks to update or change product price, stock, or both
  (e.g., "update price", "change price", "update product"),
  return UPDATE_PRODUCT.
  by selling all products (optionally with a discount), return SALES_SUMMARY.
- If the message is casual, opinion-based, or unrelated to shop operations,
  return UNKNOWN.

Message: {message}

Return only the intent.
"""
    res = llm.invoke(prompt)
    return res.content.strip()
