"""
Vulnerable test file 171
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 1710
API_KEY = "sk_live_51H7YZ2eZvKYlo2C1710"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1710"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1710"

def encrypt_1711(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

