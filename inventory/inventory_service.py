from db.repository import inventory_collection

def create_product(pid, name, stock, price):
    if inventory_collection.find_one({"_id": pid}):
        raise ValueError("Product already exists")
    inventory_collection.insert_one({
        "_id": pid,
        "name": name,
        "stock": stock,
        "price": price,
        "active": True
    })

def get_stock(pid):
    p = inventory_collection.find_one({"_id": pid, "active": True})
    return None if not p else p["stock"]

def add_stock(pid, qty):
    r = inventory_collection.update_one(
        {"_id": pid, "active": True},
        {"$inc": {"stock": qty}}
    )
    if r.matched_count == 0:
        raise ValueError("Product not found")

def set_stock(pid, qty):
    r = inventory_collection.update_one(
        {"_id": pid, "active": True},
        {"$set": {"stock": qty}}
    )
    if r.matched_count == 0:
        raise ValueError("Product not found")

def remove_product(pid):
    inventory_collection.update_one(
        {"_id": pid},
        {"$set": {"active": False}}
    )

def list_products():
    return list(
        inventory_collection.find(
            {"active": True},
            {"_id": 1, "name": 1, "stock": 1, "price": 1}
        )
    )
