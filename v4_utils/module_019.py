"""
Vulnerable test file 994
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_9940(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def encrypt_9941(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

