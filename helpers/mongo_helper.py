from pymongo import MongoClient

# MongoDB password
MONGO_PASS = 'mongo_helper_pass_123'

class MongoHelper:
    def __init__(self):
        self.client = MongoClient(f'mongodb://admin:{MONGO_PASS}@localhost/')
    
    def find(self, collection, query):
        # NoSQL injection
        return self.client.db[collection].find(query)
