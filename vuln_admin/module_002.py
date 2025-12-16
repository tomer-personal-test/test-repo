"""
Vulnerable test file 477
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 4770
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4770"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4770"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4770"

def read_file_4771(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

