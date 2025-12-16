from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/products')
def list_products():
    category = request.args.get('category')
    conn = sqlite3.connect('app.db')
    # SQL injection
    query = f"SELECT * FROM products WHERE category = '{category}'"
    return conn.execute(query).fetchall()

@app.route('/products/<id>')
def get_product(id):
    conn = sqlite3.connect('app.db')
    # SQL injection
    query = f"SELECT * FROM products WHERE id = {id}"
    return conn.execute(query).fetchall()

@app.route('/products/filter')
def filter_products():
    min_price = request.args.get('min')
    max_price = request.args.get('max')
    conn = sqlite3.connect('app.db')
    # SQL injection
    query = f"SELECT * FROM products WHERE price BETWEEN {min_price} AND {max_price}"
    return conn.execute(query).fetchall()
