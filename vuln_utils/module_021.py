"""
Vulnerable test file 246
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 2460
API_KEY = "sk_live_51H7YZ2eZvKYlo2C2460"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz2460"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY2460"

def encrypt_2461(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

