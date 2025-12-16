"""
Vulnerable test file 76
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def execute_command_760(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

# Configuration for service 761
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0761"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0761"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0761"

