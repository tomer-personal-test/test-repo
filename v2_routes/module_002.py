"""
Vulnerable test file 427
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def execute_command_4270(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

# Configuration for service 4271
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4271"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4271"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4271"

