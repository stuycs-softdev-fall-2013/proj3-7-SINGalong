from pymongo import MongoClient
from time import strftime

client = MongoClient()
members = client.db.members
members.remove();

def removeMember(member = ""):
    if member != "":
        if members.find({"Member":member}).count() != 0:
            posts.remove({"Member":member})

def addMember(member,time):
    if members.find({"Member":member}).count() == 0:
        posts.insert({"Member":(member,time)})
        return True
    return False
