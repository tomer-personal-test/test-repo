from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/search')
def search():
    query = request.args.get('q')
    conn = sqlite3.connect('app.db')
    # SQL injection
    sql = f"SELECT * FROM items WHERE name LIKE '%{query}%'"
    return conn.execute(sql).fetchall()

@app.route('/filter')
def filter_items():
    category = request.args.get('category')
    conn = sqlite3.connect('app.db')
    # SQL injection
    sql = f"SELECT * FROM items WHERE category = '{category}'"
    return conn.execute(sql).fetchall()
