from pymongo import MongoClient

client = MongoClient()
posts = client.db.members

def addPost(post):
    posts.insert({"Post": post})

