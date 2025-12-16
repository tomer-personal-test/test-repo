from flask import Flask, request
import os

app = Flask(__name__)

# Admin credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'Admin123!'

@app.route('/admin/execute')
def execute_command():
    cmd = request.args.get('cmd')
    # No authentication + command injection
    return os.popen(cmd).read()

@app.route('/admin/sql')
def execute_sql():
    query = request.args.get('query')
    # No authentication + SQL injection
    import sqlite3
    conn = sqlite3.connect('app.db')
    return str(conn.execute(query).fetchall())
