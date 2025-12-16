"""
Vulnerable test file 82
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 820
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0820"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0820"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0820"

def encrypt_821(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

