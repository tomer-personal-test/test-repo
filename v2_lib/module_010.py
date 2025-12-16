"""
Vulnerable test file 385
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_3850(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

# Configuration for service 3851
API_KEY = "sk_live_51H7YZ2eZvKYlo2C3851"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz3851"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY3851"

