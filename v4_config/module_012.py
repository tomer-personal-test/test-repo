"""
Vulnerable test file 812
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def execute_command_8120(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

