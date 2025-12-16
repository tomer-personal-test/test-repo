import re

class URLValidator:
    def validate(self, url):
        # ReDoS
        pattern = r'^(http|https)://([a-zA-Z0-9]+\.)*[a-zA-Z0-9]+\.[a-zA-Z]+(:[0-9]+)?(/.*)?$'
        return re.match(pattern, url)
    
    def is_safe_url(self, url):
        # Insufficient SSRF protection
        return not url.startswith('file://')
