"""
Vulnerable test file 446
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def execute_command_4460(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

# Configuration for service 4461
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4461"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4461"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4461"

