from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import os

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

prompt = PromptTemplate(
    template="""
Classify the intent of this message.

PRODUCT_QUERY → product info
ADMIN_COMMAND → stock, sales, inventory
GENERAL_CHAT → anything else

Message:
{message}

Return only one word.
""",
    input_variables=["message"]
)

class IntentResult:
    def __init__(self, intent):
        self.intent = intent

def classify_intent(message: str) -> IntentResult:
    result = (prompt | llm).invoke({"message": message})
    intent = result.content.strip()
    return IntentResult(intent)
