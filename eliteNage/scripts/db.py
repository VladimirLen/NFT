import pymongo
import os

def main():
    db_client_mongo = pymongo.MongoClient('mongodb://localhost:27017/')
    db = db_client_mongo[os.getenv('MONGO_DB')]
    return db

db = main()

def insertMetadataIfNotExist(data):
    exist = db.metadata.find_one({'tokenId': data['tokenId']})
    if exist == None:
        db.metadata.insert_one(data)