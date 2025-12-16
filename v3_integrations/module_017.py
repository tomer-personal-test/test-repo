"""
Vulnerable test file 617
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def encrypt_6170(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

# Configuration for service 6171
API_KEY = "sk_live_51H7YZ2eZvKYlo2C6171"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz6171"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY6171"

