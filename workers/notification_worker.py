import requests

# Notification service credentials
SLACK_WEBHOOK = 'https://hooks.slack.com/services/T00/B00/XXXX'
DISCORD_WEBHOOK = 'https://discord.com/api/webhooks/123/abc'
TWILIO_TOKEN = 'twilio_auth_token_123'

class NotificationWorker:
    def send_slack(self, message):
        # Hardcoded webhook
        requests.post(SLACK_WEBHOOK, json={'text': message})
    
    def send_discord(self, message):
        # Hardcoded webhook
        requests.post(DISCORD_WEBHOOK, json={'content': message})
