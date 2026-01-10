import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from rag.vectorstore import get_vectorstore

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2,
    api_key=os.getenv("GROQ_API_KEY")
)

with open("prompts/product_rag.txt", "r", encoding="utf-8") as f:
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
