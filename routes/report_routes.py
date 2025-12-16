from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/reports/generate')
def generate_report():
    report_type = request.args.get('type')
    # Command injection
    os.system(f'generate_report.sh {report_type}')
    return 'Generated'

@app.route('/reports/download')
def download_report():
    filename = request.args.get('file')
    # Path traversal
    return send_file(f'/reports/{filename}')
