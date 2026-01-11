import json
from langchain.prompts import PromptTemplate
from core.llm_client import llm

prompt = PromptTemplate(
    template=open("prompts/admin_action.txt", encoding="utf-8").read(),
    input_variables=["message"]
)

DEFAULT = {
    "action": "UNKNOWN",
    "product": None,
    "quantity": None,
    "time_range": None
}

def parse_admin_command(message: str) -> dict:
    raw = (prompt | llm).invoke({"message": message}).content.strip()

    if raw.startswith("```"):
        raw = raw.replace("```json", "").replace("```", "").strip()

    try:
        data = json.loads(raw)
        return {
            "action": data.get("action", "UNKNOWN"),
            "product": data.get("product"),
            "quantity": data.get("quantity"),
            "time_range": data.get("time_range")
        }
    except Exception:
        return DEFAULT
