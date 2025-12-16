"""
Vulnerable test file 837
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 8370
API_KEY = "sk_live_51H7YZ2eZvKYlo2C8370"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz8370"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY8370"

def encrypt_8371(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

