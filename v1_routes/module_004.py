"""
Vulnerable test file 179
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def execute_command_1790(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

def encrypt_1791(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

