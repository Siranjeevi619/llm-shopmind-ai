import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "shop_bot")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

inventory_col = db["inventory"]
sales_col = db["sales"]
