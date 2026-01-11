from db.mongo import inventory_collection

def handle_admin_action(action: dict) -> str:
    t = action["action"]
    product = action["product"]
    qty = action["quantity"]

    if t == "INVENTORY_ADD":
        inventory_collection.update_one(
            {"product": product},
            {"$inc": {"stock": qty}},
            upsert=True
        )
        return f"Added {qty} units to {product}"

    if t == "INVENTORY_SET":
        inventory_collection.update_one(
            {"product": product},
            {"$set": {"stock": qty}},
            upsert=True
        )
        return f"Stock for {product} set to {qty}"

    if t == "STOCK_QUERY":
        item = inventory_collection.find_one({"product": product})
        stock = item["stock"] if item else 0
        return f"Current stock for {product} is {stock}"

    return "Unknown admin action"
