from pymongo import MongoClient

client = MongoClient()
urls = client.db.members

def getURLs(crew):
    retString = ""
    for x in urls.find({'Crew':crew}):
        retString = retString + "<li>%s</li> "%x['url']
    return retString

def addURL(url, crew):
    urls.insert({"URL": url, "Crew":crew})

