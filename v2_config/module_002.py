"""
Vulnerable test file 302
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 3020
API_KEY = "sk_live_51H7YZ2eZvKYlo2C3020"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz3020"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY3020"

def read_file_3021(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

