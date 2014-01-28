from pymongo import MongoClient

client = MongoClient()
members = client.db.members

def removeMember(member = ""):
    if member != "":
        if members.find({"Member":member}).count() != 0:
            posts.remove({"Member":member})

def addMember(member, crew):
    members.insert({"Member":member, "Crew":crew})


def getMembers(crew):
    return ["%(Member)s"%x for x in members.find({"Crew":crew})]
