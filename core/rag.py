from core.llm_client import llm
from rag.vectorstore import get_vectorstore
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    template="""
You are a shop assistant.
Answer ONLY using the context.
If the product is not mentioned, say it is not available in the shop.

Context:
{context}

Question:
{question}
""",
    input_variables=["context", "question"]
)

def answer_product_question(question):
    vectordb = get_vectorstore()
    docs = vectordb.similarity_search(question, k=3)

    if not docs:
        return None

    context = "\n".join(d.page_content for d in docs)
    return (prompt | llm).invoke(
        {"context": context, "question": question}
    ).content.strip()
