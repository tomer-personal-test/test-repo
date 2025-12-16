"""
Vulnerable test file 186
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_1860(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def encrypt_1861(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

