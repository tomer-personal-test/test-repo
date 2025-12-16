"""
Vulnerable test file 447
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 4470
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4470"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4470"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4470"

def execute_command_4471(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

