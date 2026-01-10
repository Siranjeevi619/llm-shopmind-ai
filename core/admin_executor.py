from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)

db = client["shop_db"]
inventory = db["inventory"]


def execute_admin_action(action: dict) -> dict:
    action_type = action.get("action")
    product = action.get("product")
    quantity = action.get("quantity")

    if action_type == "INVENTORY_ADD":
        inventory.update_one(
            {"product": product},
            {"$inc": {"stock": quantity}},
            upsert=True
        )
        return {
            "result": f"Added {quantity} units to {product}"
        }

    if action_type == "INVENTORY_SET":
        inventory.update_one(
            {"product": product},
            {"$set": {"stock": quantity}},
            upsert=True
        )
        return {
            "result": f"Stock for {product} set to {quantity}"
        }

    if action_type == "STOCK_QUERY":
        item = inventory.find_one({"product": product})
        stock = item["stock"] if item else 0
        return {
            "result": f"Current stock for {product} is {stock}"
        }

    if action_type == "SALES_QUERY":
        return {
            "result": "Sales tracking not implemented yet"
        }

    return {
        "result": "Unknown admin action"
    }
