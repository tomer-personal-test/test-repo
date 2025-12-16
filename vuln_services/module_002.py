"""
Vulnerable test file 202
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def encrypt_2020(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

def load_data_2021(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

