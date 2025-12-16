import requests

# API credentials
API_KEY = 'api_key_1234567890abcdef'
API_SECRET = 'api_secret_abcdefghijklmnop'

class SyncWorker:
    def sync_data(self, url):
        # SSRF + hardcoded credentials
        headers = {'Authorization': f'Bearer {API_KEY}'}
        return requests.get(url, headers=headers).json()
