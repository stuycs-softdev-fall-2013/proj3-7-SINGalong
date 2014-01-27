from pymongo import MongoClient

client = MongoClient()
directors = client.db.directors
directors.remove()
