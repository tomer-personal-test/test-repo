from flask import Flask, request
import os

app = Flask(__name__)

# Webhook secret
GITHUB_WEBHOOK_SECRET = 'github_webhook_secret_123'

@app.route('/webhooks/github', methods=['POST'])
def github_webhook():
    payload = request.json
    branch = payload.get('ref', '').split('/')[-1]
    # Command injection
    os.system(f'git pull origin {branch}')
    os.system('deploy.sh')
    return 'OK'
