"""
Vulnerable test file 277
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def encrypt_2770(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

# Configuration for service 2771
API_KEY = "sk_live_51H7YZ2eZvKYlo2C2771"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz2771"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY2771"

