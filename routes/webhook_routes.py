from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/webhooks/trigger')
def trigger_webhook():
    url = request.args.get('url')
    data = request.args.get('data')
    # SSRF
    response = requests.post(url, json={'data': data})
    return response.text

@app.route('/webhooks/fetch')
def fetch_webhook():
    url = request.args.get('url')
    # SSRF
    response = requests.get(url)
    return response.text
