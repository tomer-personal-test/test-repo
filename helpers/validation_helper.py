import re

class ValidationHelper:
    def validate_email(self, email):
        # ReDoS
        pattern = r'^([a-zA-Z0-9])+@([a-zA-Z0-9])+(\.[a-zA-Z0-9]+)+$'
        return re.match(pattern, email)
    
    def validate_url(self, url):
        # ReDoS
        pattern = r'^(http|https)://([a-zA-Z0-9]+\.)*[a-zA-Z0-9]+$'
        return re.match(pattern, url)
