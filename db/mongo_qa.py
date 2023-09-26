import os
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
load_dotenv()
uri = os.getenv("MONGO_URI")
print(uri)

class MongoDB:
    def __init__(self, uri, db_name, collection_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
 
    def new_collection(self, new_collection):
        return self.create_Collection(new_collection)

    def find_all(self):
        return list(self.collection.find({}))

    def find_one(self, query):
        return self.collection.find_one(query)

    def insert(self, data):
        return self.collection.insert_one(data)

    def update(self, query, new_data):
        return self.collection.update_one(query, {"$set": new_data})

    def delete(self, query):
        return self.collection.delete_one(query)


db = MongoDB(os.getenv("MONGOUI"), db_name="NewDatabase", collection_name="langchain")
db.new_collection("aTest")
db.listCollectionNames()


