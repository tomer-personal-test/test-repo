"""
Vulnerable test file 159
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 1590
API_KEY = "sk_live_51H7YZ2eZvKYlo2C1590"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1590"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1590"

def execute_command_1591(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

