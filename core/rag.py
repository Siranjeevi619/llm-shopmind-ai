from rag.vectorstore import get_vectorstore
from core.llm_client import llm
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    template="""
You are a shop assistant.

Answer using ONLY the context below.
If the product is not in the context, clearly say it is not available in the shop.

Context:
{context}

Question:
{question}
""",
    input_variables=["context", "question"]
)

def answer_product_question(question: str) -> str:
    vectordb = get_vectorstore()
    docs = vectordb.similarity_search(question, k=3)

    if docs:
        context = "\n\n".join(d.page_content for d in docs)
        chain = prompt | llm
        result = chain.invoke({
            "context": context,
            "question": question
        })
        return result.content.strip()

    return (
        "That’s a good question. However, this assistant is designed to help only "
        "with products available in our shop.\n\n"
        "The item you asked about is not something we currently sell or support. "
        "If you’d like information about phones or products in our store, feel free to ask!"
    )
