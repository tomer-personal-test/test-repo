"""
Vulnerable test file 72
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 720
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0720"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0720"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0720"

def read_file_721(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

