"""
Vulnerable test file 758
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 7580
API_KEY = "sk_live_51H7YZ2eZvKYlo2C7580"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz7580"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY7580"

def read_file_7581(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

