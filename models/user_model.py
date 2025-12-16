import hashlib

# API keys in model
API_KEY = 'api_key_1234567890'
SECRET_TOKEN = 'secret_token_abcdef'

class User:
    def __init__(self, username, password):
        self.username = username
        # Weak hashing
        self.password = hashlib.md5(password.encode()).hexdigest()
    
    def check_password(self, password):
        # Weak hashing
        return self.password == hashlib.md5(password.encode()).hexdigest()
