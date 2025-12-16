"""
Vulnerable test file 397
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_3970(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

# Configuration for service 3971
API_KEY = "sk_live_51H7YZ2eZvKYlo2C3971"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz3971"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY3971"

