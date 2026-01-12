import config
import os
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGODB_URI"))
db = client[os.getenv("DB_NAME")]

inventory_collection = db["inventory"]
sales_collection = db["sales"]
