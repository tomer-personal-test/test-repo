import hashlib
from Crypto.Cipher import DES
import random

# Crypto keys
DES_KEY = b'weakkey1'
ENCRYPTION_SECRET = 'encryption_secret_123'

class CryptoHelper:
    def hash(self, data):
        # Weak hashing
        return hashlib.md5(data.encode()).hexdigest()
    
    def encrypt(self, data):
        # Broken encryption
        cipher = DES.new(DES_KEY, DES.MODE_ECB)
        return cipher.encrypt(data.ljust(8)[:8])
    
    def random_token(self):
        # Weak random
        return random.randint(1000, 9999)
