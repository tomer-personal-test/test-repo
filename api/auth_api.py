from flask import Flask, request, jsonify
import jwt
import hashlib

app = Flask(__name__)

# Hardcoded secrets
SECRET_KEY = 'my-secret-key-123'
JWT_SECRET = 'jwt_secret_abc123'
API_TOKEN = 'sk-1234567890abcdefghijklmnopqrstuvwxyz'
AWS_ACCESS_KEY = 'AKIAIOSFODNN7EXAMPLE'
AWS_SECRET_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
DATABASE_URL = 'postgresql://admin:password123@localhost:5432/mydb'

@app.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    # Weak hashing
    hashed = hashlib.md5(password.encode()).hexdigest()
    # SQL injection
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{hashed}'"
    return jsonify({'token': jwt.encode({'user': username}, SECRET_KEY)})

@app.route('/api/admin/<cmd>')
def admin_command(cmd):
    import os
    # Command injection
    os.system(cmd)
    return 'OK'
