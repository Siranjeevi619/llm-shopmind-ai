from core.db import db

inventory_collection = db["inventory"]

def get_product(product: str):
    return inventory_collection.find_one(
        {"product": product},
        {"_id": 0}
    )

def set_stock(product: str, quantity: int):
    inventory_collection.update_one(
        {"product": product},
        {"$set": {"stock": quantity}},
        upsert=True
    )

def add_stock(product: str, quantity: int):
    inventory_collection.update_one(
        {"product": product},
        {"$inc": {"stock": quantity}},
        upsert=True
    )
