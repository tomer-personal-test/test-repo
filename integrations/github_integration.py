import requests

# GitHub credentials
GITHUB_TOKEN = 'ghp_1234567890abcdefghijklmnopqrstuvwxyz'
GITHUB_WEBHOOK_SECRET = 'github_webhook_secret_123'

class GitHubIntegration:
    def get_repos(self, username):
        # Hardcoded token
        headers = {'Authorization': f'token {GITHUB_TOKEN}'}
        url = f'https://api.github.com/users/{username}/repos'
        # SSRF
        return requests.get(url, headers=headers).json()
