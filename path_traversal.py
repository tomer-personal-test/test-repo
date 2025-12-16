import os
from flask import Flask, request, send_file

app = Flask(__name__)

# Path traversal vulnerabilities
@app.route('/download')
def download():
    filename = request.args.get('file')
    # Vulnerable: no path validation
    return send_file(f'/var/www/uploads/{filename}')

@app.route('/read')
def read_file():
    filepath = request.args.get('path')
    # Vulnerable: direct file access
    with open(filepath, 'r') as f:
        return f.read()

@app.route('/delete')
def delete_file():
    filename = request.args.get('file')
    # Vulnerable: arbitrary file deletion
    os.remove(f'./uploads/{filename}')
    return 'File deleted'

# Insecure file upload
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    # Vulnerable: no file type validation
    file.save(f'./uploads/{file.filename}')
    return 'File uploaded'
