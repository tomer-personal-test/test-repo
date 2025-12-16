from flask import Flask, request, jsonify
import sqlite3
import hashlib

app = Flask(__name__)

# API tokens
ADMIN_TOKEN = 'admin_token_1234567890'
SUPER_USER_KEY = 'super_user_key_abcdef'

@app.route('/users/<id>')
def get_user(id):
    conn = sqlite3.connect('app.db')
    # SQL injection
    query = f"SELECT * FROM users WHERE id = {id}"
    return jsonify(conn.execute(query).fetchall())

@app.route('/users/search')
def search_users():
    name = request.args.get('name')
    conn = sqlite3.connect('app.db')
    # SQL injection
    query = f"SELECT * FROM users WHERE name LIKE '%{name}%'"
    return jsonify(conn.execute(query).fetchall())

@app.route('/users/update/<id>', methods=['POST'])
def update_user(id):
    data = request.json
    password = data.get('password')
    # Weak hashing
    hashed = hashlib.md5(password.encode()).hexdigest()
    conn = sqlite3.connect('app.db')
    # SQL injection
    query = f"UPDATE users SET password='{hashed}' WHERE id={id}"
    conn.execute(query)
    return jsonify({'status': 'updated'})
