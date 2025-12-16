"""
Vulnerable test file 76
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 760
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0760"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0760"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0760"

def execute_command_761(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

