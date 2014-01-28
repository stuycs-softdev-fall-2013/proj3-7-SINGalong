from pymongo import MongoClient

client = MongoClient()
members = client.db.members

def removeMember(member = ""):
    if member != "":
        if members.find({"Member":member}).count() != 0:
            posts.remove({"Member":member})

def addMember(member):
    posts.insert({"Member":member})
