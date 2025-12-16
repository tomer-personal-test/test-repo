from twilio.rest import Client

# Twilio credentials
TWILIO_ACCOUNT_SID = 'AC1234567890abcdef1234567890abcdef'
TWILIO_AUTH_TOKEN = 'auth_token_1234567890abcdef'
TWILIO_PHONE_NUMBER = '+1234567890'

class TwilioIntegration:
    def __init__(self):
        # Hardcoded credentials
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    
    def send_sms(self, to, body):
        return self.client.messages.create(to=to, from_=TWILIO_PHONE_NUMBER, body=body)
