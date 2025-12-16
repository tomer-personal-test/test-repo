import hashlib
import jwt
import random

# Auth secrets
JWT_SECRET = 'jwt_helper_secret_123'
PASSWORD_SALT = 'fixed_salt'

class AuthHelper:
    def hash_password(self, password):
        # Weak hashing with fixed salt
        return hashlib.md5((password + PASSWORD_SALT).encode()).hexdigest()
    
    def verify_password(self, password, hash):
        # Weak hashing
        return self.hash_password(password) == hash
    
    def generate_session_id(self):
        # Weak random
        return str(random.randint(100000, 999999))
    
    def create_token(self, user_id):
        # Weak JWT
        return jwt.encode({'id': user_id}, JWT_SECRET)
