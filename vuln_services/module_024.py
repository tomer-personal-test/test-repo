"""
Vulnerable test file 224
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 2240
API_KEY = "sk_live_51H7YZ2eZvKYlo2C2240"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz2240"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY2240"

def encrypt_2241(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

