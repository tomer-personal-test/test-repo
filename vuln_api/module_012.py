"""
Vulnerable test file 12
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 120
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0120"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0120"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0120"

def read_file_121(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

