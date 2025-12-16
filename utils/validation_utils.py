import re

def validate_email(email):
    # ReDoS vulnerability
    pattern = r'^([a-zA-Z0-9])+@([a-zA-Z0-9])+(\.[a-zA-Z0-9]+)+$'
    return re.match(pattern, email)

def validate_url(url):
    # ReDoS vulnerability
    pattern = r'^(http|https)://([a-zA-Z0-9]+\.)*[a-zA-Z0-9]+\.[a-zA-Z]+$'
    return re.match(pattern, url)

def validate_phone(phone):
    # ReDoS vulnerability
    pattern = r'^(\d{3})-(\d{3})-(\d{4})$'
    return re.match(pattern, phone)
