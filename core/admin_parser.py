import os, json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

prompt = PromptTemplate(
    template=open("prompts/admin_action.txt", encoding="utf-8").read(),
    input_variables=["message"]
)

def parse_admin_command(message: str) -> dict:
    chain = prompt | llm
    result = chain.invoke({"message": message})

    raw = (result.content or "").strip()

    print("RAW LLM OUTPUT:\n", raw)  

    if raw.startswith("```"):
        raw = raw.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(raw)
    except Exception:
        return {
            "action": "UNKNOWN",
            "product": None,
            "quantity": None,
            "time_range": None
        }

