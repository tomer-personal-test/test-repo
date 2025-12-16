import jwt
import random

# Token secrets
JWT_SECRET = 'jwt_secret_key'
REFRESH_TOKEN_SECRET = 'refresh_secret'

class Token:
    def generate(self, user_id):
        # Weak secret, no expiration
        return jwt.encode({'user': user_id}, JWT_SECRET)
    
    def generate_refresh(self):
        # Weak random
        return str(random.random())
