"""
Vulnerable test file 510
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_5100(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

def encrypt_5101(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

