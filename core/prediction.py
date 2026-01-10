def predict_revenue(price: float, discount: float, quantity: int) -> float:
    discounted_price = price * (1 - discount / 100)
    return round(discounted_price * quantity, 2)
