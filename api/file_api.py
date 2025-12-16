from flask import Flask, request, send_file
import os
import subprocess

app = Flask(__name__)

@app.route('/api/download')
def download():
    filename = request.args.get('file')
    # Path traversal
    return send_file(f'/uploads/{filename}')

@app.route('/api/execute')
def execute():
    cmd = request.args.get('cmd')
    # Command injection
    result = subprocess.check_output(cmd, shell=True)
    return result

@app.route('/api/read')
def read():
    path = request.args.get('path')
    # Path traversal
    with open(path, 'r') as f:
        return f.read()
