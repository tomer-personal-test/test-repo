from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = request.form.get('filename')
    # Path traversal + no file validation
    file.save(f'/uploads/{filename}')
    return 'Uploaded'

@app.route('/upload_exec', methods=['POST'])
def upload_exec():
    file = request.files['file']
    # Dangerous file execution
    file.save('/tmp/script.sh')
    os.system('chmod +x /tmp/script.sh && /tmp/script.sh')
    return 'Executed'
