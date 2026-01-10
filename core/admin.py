import os
import json
import re
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


def _extract_json(text: str) -> dict:
    """
    Safely extract JSON from LLM output
    """
    try:
        # Remove markdown if present
        text = re.sub(r"```.*?```", "", text, flags=re.S).strip()

        # Extract JSON object
        match = re.search(r"\{.*\}", text, flags=re.S)
        if not match:
            raise ValueError("No JSON found")

        return json.loads(match.group())
    except Exception:
        return {
            "action": "UNKNOWN",
            "product": None,
            "quantity": None,
            "time_range": None
        }


def parse_admin_command(message: str) -> dict:
    chain = prompt | llm
    result = chain.invoke({"message": message})
    return _extract_json(result.content)
