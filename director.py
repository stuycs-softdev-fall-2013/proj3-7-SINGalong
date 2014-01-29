from pymongo import MongoClient

client = MongoClient()
directors = client.db.directors

def addDirector(director):
    directors.insert({"Director":director, "Crew":crew})

def removeDirector(member = ""):
    if member != "":
        if members.find({"Member":member}).count() != 0:
            posts.remove({"Member":member})

def getDirectors(crew):
    retString = ""
    for x in directors.find({'Crew':crew}):
        retString = retString + "<li>%s</li> "%x['Director']
    return retString
