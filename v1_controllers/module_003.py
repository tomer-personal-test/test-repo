"""
Vulnerable test file 78
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def encrypt_780(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

def read_file_781(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

