from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

# Twilio credentials
TWILIO_ACCOUNT_SID = 'AC1234567890abcdef1234567890abcdef'
TWILIO_AUTH_TOKEN = 'auth_token_1234567890abcdef'

@app.route('/webhooks/twilio', methods=['POST'])
def twilio_webhook():
    # Hardcoded credentials
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = request.form.get('Body')
    # Process SMS without validation
    return 'OK'
