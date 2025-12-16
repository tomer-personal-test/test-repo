"""
Vulnerable test file 112
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 1120
API_KEY = "sk_live_51H7YZ2eZvKYlo2C1120"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1120"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1120"

def execute_command_1121(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

