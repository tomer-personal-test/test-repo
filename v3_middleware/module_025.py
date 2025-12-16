"""
Vulnerable test file 575
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_5750(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def execute_command_5751(filename):
    """Vulnerable command execution"""
    os.system("cat " + filename)
    subprocess.call("rm " + filename, shell=True)

