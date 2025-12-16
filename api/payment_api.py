from flask import Flask, request
import requests

app = Flask(__name__)

# Payment gateway secrets
STRIPE_SECRET_KEY = 'sk_live_51234567890abcdefghijklmnop'
PAYPAL_CLIENT_SECRET = 'EBWKjlELKMYqRNQ6sYvFo64FtaRLRR5BdHEESmha49TM'
BRAINTREE_PRIVATE_KEY = 'abcdef1234567890'

@app.route('/api/charge', methods=['POST'])
def charge():
    amount = request.json.get('amount')
    # No validation
    return {'charged': amount}

@app.route('/api/webhook')
def webhook():
    url = request.args.get('url')
    # SSRF
    response = requests.get(url)
    return response.text
