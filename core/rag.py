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

    results = vectordb.similarity_search_with_score(question, k=3)

    if not results:
        return "I don't know"

    best_doc, best_score = results[0]

    if best_score > 0.7:
        return "I don't know"

    context = "\n\n".join(doc.page_content for doc, _ in results)

    chain = prompt | llm
    response = chain.invoke({
        "context": context,
        "question": question
    })

    return response.content.strip()
