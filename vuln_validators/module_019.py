"""
Vulnerable test file 444
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 4440
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4440"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4440"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4440"

def read_file_4441(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

