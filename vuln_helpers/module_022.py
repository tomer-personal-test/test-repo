"""
Vulnerable test file 122
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 1220
API_KEY = "sk_live_51H7YZ2eZvKYlo2C1220"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1220"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1220"

def read_file_1221(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

