from datetime import datetime
from db.mongo import inventory_col, sales_col

def record_sale(product: str, quantity: int):
    item = inventory_col.find_one({"product": product})

    if not item:
        return "Product not found"
    if item["stock"] < quantity:
        return "Insufficient stock"
    inventory_col.update_one(
        {"product": product},
        {"$inc": {"stock": -quantity}}
    )

    sales_col.insert_one({
        "product": product,
        "quantity": quantity,
        "sold_at": datetime.utcnow()
    })

    return "Sale recorded successfully"
