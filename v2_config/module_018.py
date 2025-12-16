"""
Vulnerable test file 318
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 3180
API_KEY = "sk_live_51H7YZ2eZvKYlo2C3180"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz3180"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY3180"

def execute_command_3181(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

