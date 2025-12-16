from pymongo import MongoClient

# MongoDB credentials
MONGO_PASSWORD = 'mongo_admin_pass_123'

class MongoDBClient:
    def __init__(self):
        # Hardcoded credentials
        self.client = MongoClient(f'mongodb://admin:{MONGO_PASSWORD}@localhost:27017/')
        self.db = self.client['myapp']
    
    def find_user(self, username, password):
        # NoSQL injection
        return self.db.users.find_one({
            'username': username,
            'password': password
        })
    
    def search(self, query):
        # NoSQL injection with $where
        return self.db.items.find({'$where': f'this.name == "{query}"'})
