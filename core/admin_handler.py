from db.mongo import inventory_collection, sales_collection
from datetime import datetime, timedelta
from core.sales_prediction import predict_sales
def handle_admin_action(action: dict) -> str:
    action_type = action.get("action")
    product = action.get("product")
    quantity = action.get("quantity")
    time_range = action.get("time_range")

    if action_type == "INVENTORY_ADD":
        inventory_collection.update_one(
            {"product": product},
            {"$inc": {"stock": quantity}},
            upsert=True
        )
        return f"Added {quantity} units to {product}"

    if action_type == "INVENTORY_SET":
        inventory_collection.update_one(
            {"product": product},
            {"$set": {"stock": quantity}},
            upsert=True
        )
        return f"Stock for {product} set to {quantity}"

    if action_type == "STOCK_QUERY":
        item = inventory_collection.find_one({"product": product})
        stock = item["stock"] if item else 0
        return f"Current stock for {product} is {stock}"
    from core.sales_prediction import predict_sales

    if action_type == "SALES_PREDICTION":
        discount = action.get("quantity")
        return predict_sales(product, discount)

    if action_type == "SALES_QUERY":
        query = {"product": product}
        now = datetime.utcnow()

        if time_range == "today":
            query["timestamp"] = {
                "$gte": now.replace(hour=0, minute=0, second=0, microsecond=0)
            }

        sales = sales_collection.find(query)
        total = sum(s.get("quantity", 0) for s in sales)

        return f"Total sales for {product} is {total}"

    return "Unknown admin action"
