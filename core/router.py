import core.intents as intents
from core.permissions import check_permission
from core.validators import require
from inventory.inventory_service import (
    create_product,
    add_stock,
    set_stock,
    get_stock,
    remove_product,
    list_products,
    update_product
)
from sales.sales_service import (
    total_sales,
    predict_sales,
    calculate_discounted_earnings
)


def route(intent, payload, role):
    if intent == intents.UNKNOWN:
        return "Please clarify your request."

    if intent == intents.GENERAL_CHAT:
        return "How can I help you today?"

    if intent == intents.ADD_PRODUCT:
        check_permission(role, intent)
        require(payload, ["product_id", "name", "stock", "price"])
        create_product(
            payload["product_id"],
            payload["name"],
            payload["stock"],
            payload["price"]
        )
        return "Product added successfully."

    if intent == intents.SET_STOCK:
        check_permission(role, intent)
        require(payload, ["product_id", "quantity"])
        set_stock(payload["product_id"], payload["quantity"])
        return "Stock set."

    if intent == intents.UPDATE_PRODUCT:
        check_permission(role, intent)
        require(payload, ["product_id"])

        if "price" not in payload and "quantity" not in payload:
            raise ValueError("Provide price or quantity to update")

        update_product(
            payload["product_id"],
            price=payload.get("price"),
            stock=payload.get("quantity")
        )
        return "Product updated successfully."

    if intent == intents.LIST_PRODUCTS:
        products = list_products()
        if not products:
            return "No products are currently available."
        return "\n".join(
            f"{p['_id']} | {p['name']} | Stock: {p['stock']} | Price: {p['price']}"
            for p in products
        )

    if intent == intents.GET_STOCK:
        require(payload, ["product_id"])
        stock = get_stock(payload["product_id"])
        return "Product not available." if stock is None else f"Current stock is {stock}"

    if intent == intents.REMOVE_PRODUCT:
        check_permission(role, intent)
        require(payload, ["product_id"])
        remove_product(payload["product_id"])
        return "Product removed."

    if intent == intents.SALES_SUMMARY:
        discount = float(payload.get("discount_percent", 0))
        total = calculate_discounted_earnings(discount)
        return f"Total possible earning after {discount}% discount is {total}"

    return "Unable to process request."
