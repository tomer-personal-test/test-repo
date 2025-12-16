"""
Vulnerable test file 483
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 4830
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4830"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4830"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4830"

def execute_command_4831(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

