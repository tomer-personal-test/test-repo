import requests

# Twitter API credentials
TWITTER_API_KEY = 'twitter_api_key_1234567890abcdefghij'
TWITTER_API_SECRET = 'twitter_secret_1234567890abcdefghijklmnopqrstuvwxyz'
TWITTER_BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAABearerToken1234567890'

class TwitterIntegration:
    def get_tweets(self, username):
        # Hardcoded token + SSRF
        headers = {'Authorization': f'Bearer {TWITTER_BEARER_TOKEN}'}
        url = f'https://api.twitter.com/2/users/by/username/{username}'
        return requests.get(url, headers=headers).json()
