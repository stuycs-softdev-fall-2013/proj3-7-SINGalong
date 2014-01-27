from pymongo import MongoClient

connection = MongoClient('db.stuycs.org')
db=connection.admin
db.authenticate('softdev','softdev')

client = MongoClient()
members = client.db.members
#members.remove() 

def removeMember(member = ""):
    if member != "":
        if members.find({"Member":member}).count() != 0:
            posts.remove({"Title":title})

def removeMember(name):
    db.members.remove({'name': name})
