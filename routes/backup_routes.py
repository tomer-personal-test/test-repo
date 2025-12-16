from flask import Flask, request
import os
import subprocess

app = Flask(__name__)

@app.route('/backup/create')
def create_backup():
    path = request.args.get('path')
    # Command injection
    os.system(f'tar -czf backup.tar.gz {path}')
    return 'Backup created'

@app.route('/backup/restore')
def restore_backup():
    file = request.args.get('file')
    # Command injection
    subprocess.call(f'tar -xzf {file}', shell=True)
    return 'Restored'
