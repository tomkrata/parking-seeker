
"""Setup mongoDB"""
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://tomkrata:ecJeKf2jSthYoSBg@cluster0.ttgdvmc.mongodb.net/?retryWrites=true&w=majority")
db = client.flask_db
todos = db.todos