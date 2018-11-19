from pymongo import MongoClient

class CustomMongoClient():
    def __init__(self, uri, database_name):
        print("Attempting to connect to mongo database...")
        self.client = MongoClient(uri)
        self.database_name = database_name
        status = self.client.admin.command("serverStatus")
        if status["ok"] == 1.0:
            print("Connected to mongo database.")
        else:
            print("Failed to connect to mongo database.")
    
    def getCollection(self, name):
        return self.client[self.database_name][name]
