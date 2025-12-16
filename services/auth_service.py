import hashlib
import random
import jwt

# More secrets
JWT_KEY = 'jwt-signing-key-123'
SESSION_SECRET = 'session_secret_xyz'
ENCRYPTION_KEY = 'encryption_key_abc'

class AuthService:
    def hash_password(self, password):
        # Weak hashing
        return hashlib.md5(password.encode()).hexdigest()
    
    def generate_token(self):
        # Weak random
        return random.randint(1000, 9999)
    
    def create_jwt(self, user_id):
        # Weak secret
        return jwt.encode({'id': user_id}, 'secret', algorithm='HS256')
