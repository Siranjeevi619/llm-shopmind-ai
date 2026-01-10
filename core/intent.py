import os
from langchain.prompts import PromptTemplate
from core.llm import llm

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPT_PATH = os.path.join(BASE_DIR, "..", "prompts", "intent.txt")

with open(PROMPT_PATH, "r", encoding="utf-8") as f:
    prompt_text = f.read()

prompt = PromptTemplate(
    template=prompt_text,
    input_variables=["message"]
)

class IntentResult:
    def __init__(self, intent: str):
        self.intent = intent

    def model_dump(self):
        return {"intent": self.intent}

def classify_intent(message: str) -> IntentResult:
    chain = prompt | llm
    result = chain.invoke({"message": message})

    intent = result.content.strip().upper()

    if intent not in ["PRODUCT_QUERY", "ADMIN_COMMAND", "GENERAL_CHAT"]:
        intent = "GENERAL_CHAT"

    return IntentResult(intent)
