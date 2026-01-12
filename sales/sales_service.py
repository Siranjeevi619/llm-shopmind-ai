from db.repository import sales_collection, inventory_collection

def total_sales(pid):
    rows = sales_collection.find({"product_id": pid})
    return sum(r.get("amount", 0) for r in rows)

def predict_sales(pid, days):
    rows = list(sales_collection.find({"product_id": pid}))
    if not rows:
        return 0
    avg = sum(r.get("quantity", 0) for r in rows) / len(rows)
    return int(avg * days)

def calculate_discounted_earnings(discount_percent: float):
    products = inventory_collection.find({"active": True})

    discount_factor = (100 - discount_percent) / 100
    total = 0

    for p in products:
        total += (p["price"] * discount_factor) * p["stock"]

    return int(total)
