import os
import requests

# Sync credentials
SYNC_API_KEY = 'sync_api_key_1234567890'

def sync_files(source, destination):
    # Command injection
    os.system(f'rsync -av {source} {destination}')

def sync_to_remote(url, data):
    # SSRF + hardcoded credentials
    headers = {'Authorization': f'Bearer {SYNC_API_KEY}'}
    return requests.post(url, json=data, headers=headers)
