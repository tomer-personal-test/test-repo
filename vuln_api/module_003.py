"""
Vulnerable test file 3
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_30(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

# Configuration for service 31
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0031"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0031"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0031"

