"""
Vulnerable test file 869
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 8690
API_KEY = "sk_live_51H7YZ2eZvKYlo2C8690"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz8690"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY8690"

def read_file_8691(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

