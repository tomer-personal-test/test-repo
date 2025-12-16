import requests

# Google API credentials
GOOGLE_API_KEY = 'AIzaSyD1234567890abcdefghijklmnopqrstuv'
GOOGLE_CLIENT_ID = '1234567890-abcdefghijklmnopqrstuvwxyz123456.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'GOCSPX-abcdefghijklmnopqrstuvwxyz'

class GoogleIntegration:
    def search(self, query):
        # Hardcoded API key
        url = f'https://www.googleapis.com/customsearch/v1?key={GOOGLE_API_KEY}&q={query}'
        # SSRF
        return requests.get(url).json()
