from db.mongo import inventory_collection

def find_product(text):
    text = text.lower()
    for item in inventory_collection.find({}, {"product": 1}):
        if item["product"].lower() in text:
            return item["product"]
    return None

def list_products():
    return [p["product"] for p in inventory_collection.find({}, {"product": 1})]
