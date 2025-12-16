"""
Vulnerable test file 941
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def execute_command_9410(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

def encrypt_9411(data):
    """Weak encryption"""
    from Crypto.Cipher import DES
    key = b'weak_key'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

