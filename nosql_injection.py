from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['myapp']

# NoSQL injection vulnerabilities
@app.route('/user')
def get_user():
    username = request.args.get('username')
    password = request.args.get('password')
    
    # Vulnerable: NoSQL injection
    user = db.users.find_one({
        'username': username,
        'password': password
    })
    return str(user)

@app.route('/search')
def search():
    query = request.args.get('q')
    
    # Vulnerable: operator injection
    results = db.products.find({'$where': f'this.name == "{query}"'})
    return str(list(results))

@app.route('/update')
def update_user():
    user_id = request.args.get('id')
    new_data = request.json
    
    # Vulnerable: unvalidated update
    db.users.update_one({'_id': user_id}, {'$set': new_data})
    return 'Updated'
