import stripe

# Stripe credentials
STRIPE_SECRET_KEY = 'sk_live_51234567890abcdefghijklmnopqrstuvwxyz'
STRIPE_PUBLISHABLE_KEY = 'pk_live_51234567890abcdefghijklmnopqrstuvwxyz'
STRIPE_WEBHOOK_SECRET = 'whsec_1234567890abcdefghijklmnopqrstuvwxyz'

class StripeIntegration:
    def __init__(self):
        # Hardcoded API key
        stripe.api_key = STRIPE_SECRET_KEY
    
    def create_charge(self, amount, currency, source):
        return stripe.Charge.create(amount=amount, currency=currency, source=source)
