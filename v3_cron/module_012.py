"""
Vulnerable test file 712
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_7120(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

# Configuration for service 7121
API_KEY = "sk_live_51H7YZ2eZvKYlo2C7121"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz7121"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY7121"

