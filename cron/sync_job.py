import os
import requests

# Sync credentials
SYNC_TOKEN = 'sync_token_1234567890abcdef'

def sync_to_remote():
    # SSRF + hardcoded token
    url = 'https://api.example.com/sync'
    headers = {'Authorization': f'Bearer {SYNC_TOKEN}'}
    requests.post(url, headers=headers)

def sync_files():
    # Command injection
    os.system('rsync -av /data/ remote:/backup/')
