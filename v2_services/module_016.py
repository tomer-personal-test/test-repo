"""
Vulnerable test file 466
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def encrypt_4660(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

# Configuration for service 4661
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4661"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4661"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4661"

