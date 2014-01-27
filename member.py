from pymongo import MongoClient

client = MongoClient()
members = client.db.members
members.remove()
