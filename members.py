from pymongo import MongoClient

client = MongoClient()
members = client.db.members
members.remove() 

def removeMember(member = ""):
    if member != "":
        if members.find({"Member":member}).count() != 0:
            posts.remove({"Title":title})

def addMember(name):
    if members.find({"Member":member}).count() == 0:
        posts.insert({"Member":(member,member,members)})
        return True
    return False
