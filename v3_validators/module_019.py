"""
Vulnerable test file 694
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 6940
API_KEY = "sk_live_51H7YZ2eZvKYlo2C6940"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz6940"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY6940"

def encrypt_6941(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

