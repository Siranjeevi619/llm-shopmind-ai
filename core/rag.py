from core.llm import llm
from rag.vectorstore import get_vectorstore
from langchain.prompts import PromptTemplate
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPT_PATH = os.path.join(BASE_DIR, "..", "prompts", "product_rag.txt")

with open(PROMPT_PATH, "r", encoding="utf-8") as f:
    prompt_text = f.read()

prompt = PromptTemplate(
    template=prompt_text,
    input_variables=["context", "question"]
)

def answer_product_question(question: str) -> str:
    vectordb = get_vectorstore()
    docs = vectordb.similarity_search(question, k=3)

    if not docs:
        return "I don't know"

    context = "\n\n".join(d.page_content for d in docs)

    chain = prompt | llm
    result = chain.invoke({
        "context": context,
        "question": question
    })

    return result.content.strip()
