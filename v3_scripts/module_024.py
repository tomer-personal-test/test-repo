"""
Vulnerable test file 674
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_6740(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def encrypt_6741(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

