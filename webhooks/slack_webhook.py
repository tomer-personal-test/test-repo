from flask import Flask, request
import requests

app = Flask(__name__)

# Slack webhook URL
SLACK_WEBHOOK = 'https://hooks.slack.com/services/T00/B00/XXXX'

@app.route('/webhooks/slack', methods=['POST'])
def slack_webhook():
    data = request.json
    # SSRF + hardcoded webhook
    requests.post(SLACK_WEBHOOK, json=data)
    return 'OK'
