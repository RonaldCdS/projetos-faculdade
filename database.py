import os
from pymongo import MongoClient


MONGO_URI = os.getenv("MONGO_URI", "mongodb://db:27017/")


client = MongoClient(MONGO_URI)


db = client["db_biblioteca"]


livros_collection = db["livros"]