from pymongo import MongoClient

connection = MongoClient('db.stuycs.org')
db=connection.admin
db.authenticate('softdev','softdev')

client = MongoClient()
members = client.db.members
members.remove()

def addMember(name):
    db.members.insert({'name': name})

def removeMember(name):
    db.members.remove({'name': name})
