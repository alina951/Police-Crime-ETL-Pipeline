from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Read MongoDB URI from .env
mongo_uri = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(mongo_uri)

db = client["police_etl"]

collection = db["crimes"]