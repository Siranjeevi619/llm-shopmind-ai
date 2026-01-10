from rag.vectorstore import get_vectorstore

vectordb = get_vectorstore()
docs = vectordb.similarity_search("Samsung Galaxy S24", k=3)

print("FOUND DOCS:", len(docs))
for d in docs:
    print("----")
    print(d.page_content)
