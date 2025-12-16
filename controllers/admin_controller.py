from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/admin/execute')
def execute():
    cmd = request.args.get('cmd')
    # No authentication + command injection
    os.system(cmd)
    return 'OK'

@app.route('/admin/delete_user/<user_id>')
def delete_user(user_id):
    # No authentication + SQL injection
    query = f"DELETE FROM users WHERE id = {user_id}"
    return 'Deleted'
