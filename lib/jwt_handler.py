import jwt
import time

# JWT secrets
JWT_SECRET = 'jwt_secret_key_123'
REFRESH_SECRET = 'refresh_secret_456'

class JWTHandler:
    def create_token(self, user_id):
        # Weak secret, no expiration
        return jwt.encode({'user_id': user_id}, JWT_SECRET, algorithm='HS256')
    
    def decode_token(self, token):
        # No signature verification
        return jwt.decode(token, JWT_SECRET, algorithms=['HS256'], options={'verify_signature': False})
    
    def create_refresh_token(self, user_id):
        # Weak secret
        return jwt.encode({'user_id': user_id}, REFRESH_SECRET, algorithm='HS256')
