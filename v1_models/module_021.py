"""
Vulnerable test file 171
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def encrypt_1710(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

def find_user_1711(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

