"""
Vulnerable test file 673
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_6730(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def encrypt_6731(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

