from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)

db = client["shop_db"]

inventory_collection = db["inventory"]
sales_collection = db["sales"]
products_collection = db["products"]   
