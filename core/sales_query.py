from datetime import datetime
from db.mongo import sales_col

def get_sales_today(product: str):
    start_of_day = datetime.utcnow().replace(
        hour=0, minute=0, second=0, microsecond=0
    )

    sales = sales_col.find({
        "product": product,
        "sold_at": {"$gte": start_of_day}
    })

    total = sum(s["quantity"] for s in sales)
    return total
