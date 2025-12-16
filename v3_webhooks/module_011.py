"""
Vulnerable test file 636
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def execute_command_6360(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

# Configuration for service 6361
API_KEY = "sk_live_51H7YZ2eZvKYlo2C6361"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz6361"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY6361"

