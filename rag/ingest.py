from rag.vectorstore import get_vectorstore

def ingest_products(products: list):
    vectordb = get_vectorstore()

    texts = []
    metadatas = []
    ids = []

    for p in products:
        text = f"""
        Product: {p['name']}
        Brand: {p['brand']}
        Category: {p['category']}
        Description: {p['description']}
        Features: {', '.join(p['features'])}
        """
        texts.append(text)
        metadatas.append({"product": p["name"]})
        ids.append(p["id"])

    vectordb.add_texts(texts=texts, metadatas=metadatas, ids=ids)
    vectordb.persist()
