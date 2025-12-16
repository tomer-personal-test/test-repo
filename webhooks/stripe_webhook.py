from flask import Flask, request
import stripe

app = Flask(__name__)

# Stripe webhook secret
STRIPE_WEBHOOK_SECRET = 'whsec_1234567890abcdefghijklmnopqrstuvwxyz'
STRIPE_API_KEY = 'sk_live_51234567890abcdefghijklmnopqrstuvwxyz'

@app.route('/webhooks/stripe', methods=['POST'])
def stripe_webhook():
    # Hardcoded API key
    stripe.api_key = STRIPE_API_KEY
    payload = request.data
    # Process payment without proper verification
    return 'OK'
