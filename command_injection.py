import os
import subprocess
from flask import Flask, request

app = Flask(__name__)

# Command injection vulnerabilities
@app.route('/ping')
def ping():
    host = request.args.get('host')
    # Vulnerable: user input in os.system
    os.system(f'ping -c 4 {host}')
    return 'Ping executed'

@app.route('/backup')
def backup():
    filename = request.args.get('file')
    # Vulnerable: shell=True with user input
    subprocess.call(f'tar -czf backup.tar.gz {filename}', shell=True)
    return 'Backup created'

@app.route('/convert')
def convert():
    input_file = request.args.get('input')
    output_file = request.args.get('output')
    # Vulnerable: direct command execution
    cmd = f'convert {input_file} {output_file}'
    os.popen(cmd).read()
    return 'Conversion complete'

# Insecure deserialization
import pickle

@app.route('/load')
def load_data():
    data = request.args.get('data')
    # Vulnerable: pickle.loads with user input
    obj = pickle.loads(data.encode())
    return str(obj)
