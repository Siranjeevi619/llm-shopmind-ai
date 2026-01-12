from bson import ObjectId
from db.mongo import db

collection = db.products


async def get_by_id(pid: str):
    try:
        return await collection.find_one({"_id": ObjectId(pid)})
    except Exception:
        return None


async def get_by_name(name: str):
    return await collection.find_one(
        {"name": {"$regex": f"^{name}$", "$options": "i"}}
    )


async def list_products():
    products = []
    async for product in collection.find():
        product["_id"] = str(product["_id"])
        products.append(product)
    return products


async def update(query: dict, update: dict):
    if "_id" in query:
        try:
            query["_id"] = ObjectId(query["_id"])
        except Exception:
            return
    await collection.update_one(query, {"$set": update})
