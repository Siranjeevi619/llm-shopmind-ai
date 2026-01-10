import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

with open("prompts/admin_action.txt", "r", encoding="utf-8") as f:
    prompt_text = f.read()

prompt = PromptTemplate(
    template=prompt_text,
    input_variables=["message"]
)

DEFAULT_RESPONSE = {
    "action": "UNKNOWN",
    "product": None,
    "quantity": None,
    "time_range": None
}

def parse_admin_command(message: str) -> dict:
    chain = prompt | llm
    result = chain.invoke({"message": message})

    raw = (result.content or "").strip()

    # Remove markdown fences if any
    if raw.startswith("```"):
        raw = raw.replace("```json", "").replace("```", "").strip()

    try:
        data = json.loads(raw)

        # Enforce schema
        return {
            "action": data.get("action", "UNKNOWN"),
            "product": data.get("product"),
            "quantity": data.get("quantity"),
            "time_range": data.get("time_range")
        }

    except Exception:
        print("ADMIN PARSE ERROR:\n", raw)
        return DEFAULT_RESPONSE
