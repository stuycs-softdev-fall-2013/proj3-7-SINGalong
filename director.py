from pymongo import MongoClient

connection = MongoClient('db.stuycs.org')
db=connection.admin
db.authenticate('softdev','softdev')

client = MongoClient()
directors = client.db.directors
#directors.remove() what is this for?

def addDirector(name, crew):
    db.directors.insert({'name': name, 'crew':crew})

def removeDirector(name):
    db.directors.remove({'name': name})
