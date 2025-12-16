"""
Vulnerable test file 130
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 1300
API_KEY = "sk_live_51H7YZ2eZvKYlo2C1300"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1300"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1300"

def read_file_1301(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

