from flask import Flask, request
import sqlite3
import pickle

app = Flask(__name__)

# More hardcoded credentials
DB_PASSWORD = 'SuperSecret123!'
SMTP_PASSWORD = 'email_pass_456'
REDIS_PASSWORD = 'redis123'

@app.route('/api/users/<user_id>')
def get_user(user_id):
    conn = sqlite3.connect('app.db')
    # SQL injection
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return conn.execute(query).fetchall()

@app.route('/api/search')
def search():
    term = request.args.get('q')
    conn = sqlite3.connect('app.db')
    # SQL injection
    query = "SELECT * FROM products WHERE name LIKE '%" + term + "%'"
    return conn.execute(query).fetchall()

@app.route('/api/deserialize', methods=['POST'])
def deserialize():
    data = request.data
    # Insecure deserialization
    obj = pickle.loads(data)
    return str(obj)
