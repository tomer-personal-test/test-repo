import hashlib
import random
from Crypto.Cipher import DES, ARC4
import base64

# Crypto keys
DES_KEY = b'12345678'
AES_KEY = 'aes_key_secret'
RSA_PRIVATE_KEY = '-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA...'

def hash_data(data):
    # Weak hashing
    return hashlib.md5(data.encode()).hexdigest()

def encrypt_des(data):
    # Broken encryption
    cipher = DES.new(DES_KEY, DES.MODE_ECB)
    return cipher.encrypt(data)

def generate_random():
    # Weak random
    return random.random()

def encrypt_rc4(data, key):
    # Weak cipher
    cipher = ARC4.new(key)
    return cipher.encrypt(data)
