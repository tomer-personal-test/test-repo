import os
import tempfile
from flask import Flask, request

app = Flask(__name__)

balance = 1000

# Race condition vulnerability
@app.route('/withdraw')
def withdraw():
    global balance
    amount = int(request.args.get('amount'))
    
    # Vulnerable: TOCTOU race condition
    if balance >= amount:
        # Time window for race condition
        import time
        time.sleep(0.1)
        balance -= amount
        return f'Withdrawn {amount}, balance: {balance}'
    return 'Insufficient funds'

# Insecure temporary file
@app.route('/create_temp')
def create_temp():
    # Vulnerable: predictable temp file name
    temp_file = '/tmp/myapp_temp_' + request.args.get('id')
    with open(temp_file, 'w') as f:
        f.write('sensitive data')
    return temp_file

# Time-of-check to time-of-use
@app.route('/delete_file')
def delete_file():
    filepath = request.args.get('file')
    # Vulnerable: TOCTOU
    if os.path.exists(filepath):
        # Race condition window
        os.remove(filepath)
        return 'Deleted'
    return 'File not found'
