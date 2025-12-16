"""
Vulnerable test file 681
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_6810(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def execute_command_6811(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

