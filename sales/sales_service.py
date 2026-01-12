from db.repository import sales_collection

def total_sales(pid):
    rows = sales_collection.find({"product_id": pid})
    return sum(r.get("amount", 0) for r in rows)

def predict_sales(pid, days):
    rows = list(sales_collection.find({"product_id": pid}))
    if not rows:
        return 0
    avg = sum(r.get("quantity", 0) for r in rows) / len(rows)
    return int(avg * days)
