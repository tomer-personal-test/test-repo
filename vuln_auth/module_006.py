"""
Vulnerable test file 31
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 310
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0310"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0310"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0310"

def encrypt_311(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

