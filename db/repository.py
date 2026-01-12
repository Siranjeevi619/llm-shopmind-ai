import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")

if not MONGODB_URI:
    raise RuntimeError("MONGODB_URI is not set in environment variables")

if not DB_NAME:
    raise RuntimeError("DB_NAME is not set in environment variables")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

inventory_collection = db["inventory"]
sales_collection = db["sales"]
