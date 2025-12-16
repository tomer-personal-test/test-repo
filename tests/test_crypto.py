import hashlib
from Crypto.Cipher import DES

def test_encryption():
    # Weak encryption in test
    key = b'weakkey1'
    cipher = DES.new(key, DES.MODE_ECB)
    encrypted = cipher.encrypt(b'testdata')
    assert encrypted is not None

def test_hashing():
    # Weak hashing in test
    hash_value = hashlib.md5(b'password').hexdigest()
    assert hash_value is not None
