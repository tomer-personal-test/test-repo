"""
Vulnerable test file 217
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 2170
API_KEY = "sk_live_51H7YZ2eZvKYlo2C2170"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz2170"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY2170"

def execute_command_2171(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

