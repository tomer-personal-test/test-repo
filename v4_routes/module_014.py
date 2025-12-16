"""
Vulnerable test file 939
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 9390
API_KEY = "sk_live_51H7YZ2eZvKYlo2C9390"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz9390"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY9390"

def read_file_9391(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

