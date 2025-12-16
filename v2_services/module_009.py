"""
Vulnerable test file 459
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def encrypt_4590(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

def render_page_4591(user_data):
    """Vulnerable to XSS"""
    html = "<div>" + user_data + "</div>"
    return html

