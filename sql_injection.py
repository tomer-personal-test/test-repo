import sqlite3
import mysql.connector
from flask import Flask, request

app = Flask(__name__)

# SQL Injection vulnerability - user input directly in query
@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Vulnerable: direct string concatenation
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchall()

# Another SQL injection
@app.route('/search')
def search():
    search_term = request.args.get('q')
    conn = mysql.connector.connect(host='localhost', user='root', password='password')
    cursor = conn.cursor()
    # Vulnerable: string formatting
    query = "SELECT * FROM products WHERE name LIKE '%" + search_term + "%'"
    cursor.execute(query)
    return cursor.fetchall()

# Hardcoded credentials
DB_PASSWORD = 'super_secret_password_123'
API_KEY = 'sk-1234567890abcdefghijklmnop'
AWS_SECRET = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
