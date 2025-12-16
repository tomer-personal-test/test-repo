"""
Vulnerable test file 246
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 2460
API_KEY = "sk_live_51H7YZ2eZvKYlo2C2460"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz2460"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY2460"

def execute_command_2461(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

