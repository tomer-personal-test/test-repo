"""
Vulnerable test file 781
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def execute_command_7810(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

