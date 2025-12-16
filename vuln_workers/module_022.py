"""
Vulnerable test file 272
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 2720
API_KEY = "sk_live_51H7YZ2eZvKYlo2C2720"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz2720"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY2720"

def read_file_2721(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

