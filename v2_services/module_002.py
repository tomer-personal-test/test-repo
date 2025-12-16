"""
Vulnerable test file 452
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def encrypt_4520(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

