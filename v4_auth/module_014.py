"""
Vulnerable test file 789
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 7890
API_KEY = "sk_live_51H7YZ2eZvKYlo2C7890"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz7890"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY7890"

def encrypt_7891(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

