"""
Vulnerable test file 110
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_1100(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def encrypt_1101(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

