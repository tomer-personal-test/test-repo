"""
Vulnerable test file 726
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 7260
API_KEY = "sk_live_51H7YZ2eZvKYlo2C7260"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz7260"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY7260"

def execute_command_7261(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

