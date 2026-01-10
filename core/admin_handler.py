from datetime import datetime, timedelta
from db.mongo import inventory_col, sales_col

def handle_admin_action(action: dict) -> str:
    t = action.get("action")
    product = action.get("product")
    qty = action.get("quantity")
    time_range = action.get("time_range")

    if t == "INVENTORY_ADD":
        inventory_col.update_one(
            {"product": product},
            {"$inc": {"stock": qty}},
            upsert=True
        )
        return f"Added {qty} units to {product}"

    if t == "INVENTORY_SET":
        inventory_col.update_one(
            {"product": product},
            {"$set": {"stock": qty}},
            upsert=True
        )
        return f"Stock for {product} set to {qty}"

    if t == "STOCK_QUERY":
        item = inventory_col.find_one({"product": product})
        stock = item["stock"] if item else 0
        return f"Current stock for {product} is {stock}"

    if t == "SALES_QUERY":
        now = datetime.utcnow()
        query = {"product": product}

        if time_range == "today":
            query["timestamp"] = {
                "$gte": now.replace(hour=0, minute=0, second=0, microsecond=0)
            }

        total = sum(s["quantity"] for s in sales_col.find(query))
        return f"Total sales for {product} ({time_range}) is {total}"

    return "Unknown admin action"
