"""
Vulnerable test file 647
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def execute_command_6470(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

# Configuration for service 6471
API_KEY = "sk_live_51H7YZ2eZvKYlo2C6471"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz6471"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY6471"

