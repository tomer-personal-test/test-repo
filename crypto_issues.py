import hashlib
import random
from Crypto.Cipher import DES, AES
import base64

# Weak cryptography
def hash_password(password):
    # Vulnerable: MD5 is broken
    return hashlib.md5(password.encode()).hexdigest()

def hash_password_sha1(password):
    # Vulnerable: SHA1 is weak
    return hashlib.sha1(password.encode()).hexdigest()

# Weak random number generation
def generate_token():
    # Vulnerable: predictable random
    return random.randint(1000, 9999)

def generate_session_id():
    # Vulnerable: weak randomness for security
    return str(random.random())

# Weak encryption
def encrypt_data(data, key):
    # Vulnerable: DES is broken
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

# Hardcoded secrets
SECRET_KEY = 'my_secret_key_12345'
JWT_SECRET = 'jwt_secret_token_abc'
ENCRYPTION_KEY = b'12345678'  # 8 bytes for DES

# Insecure SSL/TLS
import ssl
import urllib.request

def fetch_data(url):
    # Vulnerable: SSL verification disabled
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    return response.read()
