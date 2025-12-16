import requests

# Facebook credentials
FACEBOOK_APP_ID = '1234567890123456'
FACEBOOK_APP_SECRET = 'facebook_secret_abcdefghijklmnopqrstuvwxyz'
FACEBOOK_ACCESS_TOKEN = 'EAABwzLixnjYBO1234567890abcdefghijklmnop'

class FacebookIntegration:
    def get_user(self, user_id):
        # Hardcoded token + SSRF
        url = f'https://graph.facebook.com/{user_id}?access_token={FACEBOOK_ACCESS_TOKEN}'
        return requests.get(url).json()
