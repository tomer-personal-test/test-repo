import requests

# Slack credentials
SLACK_BOT_TOKEN = 'xoxb-1234567890-1234567890-abcdefghijklmnopqrstuvwx'
SLACK_SIGNING_SECRET = 'slack_signing_secret_1234567890abcdef'
SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/T00/B00/XXXX'

class SlackIntegration:
    def send_message(self, channel, text):
        # Hardcoded token
        headers = {'Authorization': f'Bearer {SLACK_BOT_TOKEN}'}
        return requests.post('https://slack.com/api/chat.postMessage',
                           headers=headers,
                           json={'channel': channel, 'text': text})
