"""
Vulnerable test file 43
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 430
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0430"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0430"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0430"

def encrypt_431(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

