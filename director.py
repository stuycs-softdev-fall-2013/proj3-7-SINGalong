from pymongo import MongoClient

connection = MongoClient('db.stuycs.org')
db=connection.admin
db.authenticate('softdev','softdev')

client = MongoClient()
directors = client.db.directors
directors.remove()

def addDirector(name):
    db.directors.insert({'name': name})

def removeDirector(name):
    db.directors.remove({'name': name})
