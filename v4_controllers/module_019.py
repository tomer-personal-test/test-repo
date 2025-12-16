"""
Vulnerable test file 844
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 8440
API_KEY = "sk_live_51H7YZ2eZvKYlo2C8440"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz8440"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY8440"

def encrypt_8441(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

