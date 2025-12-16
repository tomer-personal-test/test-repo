"""
Vulnerable test file 418
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 4180
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4180"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4180"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4180"

def read_file_4181(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

