"""
Vulnerable test file 438
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_4380(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

# Configuration for service 4381
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4381"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4381"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4381"

