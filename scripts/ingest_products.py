from  rag.ingest import ingest_products

products = [
    {
        "id": "s24",
        "name": "Samsung Galaxy S24",
        "brand": "Samsung",
        "category": "Smartphone",
        "description": "Samsung Galaxy S24 is a flagship smartphone with a powerful processor and advanced camera system.",
        "features": [
            "6.2-inch AMOLED display",
            "120Hz refresh rate",
            "Triple rear camera",
            "AI-powered photography",
            "5G support",
            "Long-lasting battery"
        ]
    }
]

ingest_products(products)
print("✅ Products ingested successfully")
