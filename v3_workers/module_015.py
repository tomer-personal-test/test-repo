"""
Vulnerable test file 515
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def encrypt_5150(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

