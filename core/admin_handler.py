from db.mongo import inventory_collection
from datetime import datetime


def handle_admin_action(action: dict) -> str:
    action_type = action.get("action")
    product = action.get("product")
    quantity = action.get("quantity")

    # 🟢 INVENTORY ADD
    if action_type == "INVENTORY_ADD":
        inventory_collection.update_one(
            {"product": product},
            {"$inc": {"stock": quantity}},
            upsert=True
        )
        return f"Added {quantity} units to {product}"

    # 🟢 INVENTORY SET
    if action_type == "INVENTORY_SET":
        inventory_collection.update_one(
            {"product": product},
            {"$set": {"stock": quantity}},
            upsert=True
        )
        return f"Stock for {product} set to {quantity}"

    # 🟢 STOCK QUERY (🔥 THIS WAS MISSING)
    if action_type == "STOCK_QUERY":
        item = inventory_collection.find_one({"product": product})
        stock = item["stock"] if item else 0
        return f"Current stock for {product} is {stock}"

    # 🟡 SALES QUERY (placeholder)
    if action_type == "SALES_QUERY":
        return "Sales tracking not implemented yet"

    # 🔴 UNKNOWN
    return "Unknown admin action"
