from datetime import datetime, timedelta
from db.mongo import sales_collection, products_collection

def predict_sales(product: str, discount: float, days: int = 30):
    product_doc = products_collection.find_one({"product": product})

    if not product_doc:
        return "This product is not available in the shop catalog."

    price = product_doc["price"]
    cost_price = product_doc.get("cost_price", price * 0.7)

    start_date = datetime.utcnow() - timedelta(days=30)

    sales = sales_collection.find({
        "product": product,
        "timestamp": {"$gte": start_date}
    })

    total_units = sum(s["quantity"] for s in sales)
    avg_daily_sales = total_units / 30 if total_units > 0 else 1

    if discount <= 5:
        boost = 1.05
    elif discount <= 10:
        boost = 1.15
    elif discount <= 20:
        boost = 1.3
    else:
        boost = 1.5

    discounted_price = price * (1 - discount / 100)
    expected_units = int(avg_daily_sales * boost * days)

    revenue = int(expected_units * discounted_price)
    profit = int(expected_units * (discounted_price - cost_price))

    return (
        f"If you offer {product} with a {discount}% discount for {days} days, "
        f"you may sell approximately {expected_units} units.\n\n"
        f"Estimated revenue would be around ₹{revenue:,}, "
        f"with an expected profit of ₹{profit:,}."
    )
