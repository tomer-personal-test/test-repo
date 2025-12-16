from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/webhooks/generic', methods=['POST'])
def generic_webhook():
    callback_url = request.json.get('callback_url')
    data = request.json.get('data')
    # SSRF
    response = requests.post(callback_url, json=data)
    return response.text
