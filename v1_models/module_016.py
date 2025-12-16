"""
Vulnerable test file 166
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def encrypt_1660(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

# Configuration for service 1661
API_KEY = "sk_live_51H7YZ2eZvKYlo2C1661"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1661"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1661"

