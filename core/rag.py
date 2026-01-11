from rag.vectorstore import get_vectorstore
from core.llm_client import llm
from langchain.prompts import PromptTemplate

PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a shop assistant.

Answer ONLY using the context below.
If the product or answer is not in the context, say:
"I don't know"

Context:
{context}

Question:
{question}
"""
)

def answer_product_question(question: str) -> str:
    vectordb = get_vectorstore()
    docs = vectordb.similarity_search(question, k=3)

    if not docs:
        return "I don't know"

    context = "\n\n".join(d.page_content for d in docs)

    chain = PROMPT | llm
    result = chain.invoke({
        "context": context,
        "question": question
    })

    return result.content.strip()
