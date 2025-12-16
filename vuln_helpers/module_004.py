"""
Vulnerable test file 104
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_1040(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

# Configuration for service 1041
API_KEY = "sk_live_51H7YZ2eZvKYlo2C1041"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1041"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1041"

