"""
Vulnerable test file 145
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_1450(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

# Configuration for service 1451
API_KEY = "sk_live_51H7YZ2eZvKYlo2C1451"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1451"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1451"

