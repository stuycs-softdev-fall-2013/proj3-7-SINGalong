from pymongo import MongoClient

client = MongoClient()
members = client.db.members

def getMembers(crew):
    retString = ""
    for x in members.find({'Crew':crew}):
        retString = retString + "<li>%s</li> "%x['Member']
    return retString

def removeMember(member = ""):
    if member != "":
        if members.find({"Member":member}).count() != 0:
            posts.remove({"Member":member})

def addMember(member, crew):
    members.insert({"Member":member, "Crew":crew})

