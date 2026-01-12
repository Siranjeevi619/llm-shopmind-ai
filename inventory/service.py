from app.inventory import repository


async def list_products():
    return await repository.list_products()


async def add_stock(product_id: str, quantity: int):
    product = await repository.get_by_id(product_id)
    if not product:
        return None

    new_stock = product["stock"] + quantity

    await repository.update(
        {"_id": product_id},
        {"stock": new_stock}
    )

    return {
        "product_id": product_id,
        "new_stock": new_stock
    }


async def describe_product(product: dict):
    return {
        "name": product["name"],
        "price": product["price"],
        "stock": product["stock"],
        "description": product.get("description")
    }
