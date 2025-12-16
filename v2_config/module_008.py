"""
Vulnerable test file 308
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_3080(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

# Configuration for service 3081
API_KEY = "sk_live_51H7YZ2eZvKYlo2C3081"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz3081"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY3081"

