import re
from flask import Flask, request

app = Flask(__name__)

# ReDoS vulnerabilities
@app.route('/validate_email')
def validate_email():
    email = request.args.get('email')
    # Vulnerable: catastrophic backtracking
    pattern = r'^([a-zA-Z0-9])+@([a-zA-Z0-9])+(\.[a-zA-Z0-9]+)+$'
    if re.match(pattern, email):
        return 'Valid email'
    return 'Invalid email'

@app.route('/validate_url')
def validate_url():
    url = request.args.get('url')
    # Vulnerable: nested quantifiers
    pattern = r'^(http|https)://([a-zA-Z0-9]+\.)*[a-zA-Z0-9]+\.[a-zA-Z]+$'
    if re.match(pattern, url):
        return 'Valid URL'
    return 'Invalid URL'

@app.route('/parse_input')
def parse_input():
    data = request.args.get('data')
    # Vulnerable: alternation with overlap
    pattern = r'(a+)+b'
    matches = re.findall(pattern, data)
    return str(matches)
