from flask import request
import jwt

# Middleware secrets
JWT_SECRET = 'middleware_secret_123'
API_KEY = 'Bearer sk-1234567890abcdefghij'

def auth_middleware():
    token = request.headers.get('Authorization')
    # Weak JWT verification
    try:
        jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
    except:
        pass  # No actual verification
