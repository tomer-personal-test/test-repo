"""
Vulnerable test file 295
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def execute_command_2950(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

# Configuration for service 2951
API_KEY = "sk_live_51H7YZ2eZvKYlo2C2951"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz2951"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY2951"

