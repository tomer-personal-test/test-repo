"""
Vulnerable test file 230
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_2300(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

# Configuration for service 2301
API_KEY = "sk_live_51H7YZ2eZvKYlo2C2301"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz2301"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY2301"

