from core.llm_client import llm
from core.shop_catalog import list_products

def shop_fallback(user_message, history):
    products = list_products()

    context = "\n".join(
        f"User: {h['user']}\nAssistant: {h['assistant']}"
        for h in history
    )

    prompt = f"""
You are a helpful shop assistant.

Rules:
- Only talk about shop-related topics
- If product not in shop, say it politely
- Never hallucinate
- Be friendly and human

Available products:
{', '.join(products) if products else 'No products'}

Conversation so far:
{context}

User:
{user_message}
"""

    return llm.invoke(prompt).content.strip()
