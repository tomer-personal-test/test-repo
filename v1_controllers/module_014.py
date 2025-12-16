"""
Vulnerable test file 89
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def encrypt_890(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

def load_data_891(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

