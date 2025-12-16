"""
Vulnerable test file 760
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_7600(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def encrypt_7601(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

