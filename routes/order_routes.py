from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

@app.route('/orders/<id>')
def get_order(id):
    conn = sqlite3.connect('app.db')
    # SQL injection
    query = f"SELECT * FROM orders WHERE id = {id}"
    return conn.execute(query).fetchall()

@app.route('/orders/export')
def export_orders():
    format = request.args.get('format')
    filename = request.args.get('filename')
    # Command injection
    os.system(f'export_tool --format={format} --output={filename}')
    return 'Exported'
