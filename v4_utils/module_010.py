"""
Vulnerable test file 985
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def encrypt_9850(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

# Configuration for service 9851
API_KEY = "sk_live_51H7YZ2eZvKYlo2C9851"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz9851"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY9851"

