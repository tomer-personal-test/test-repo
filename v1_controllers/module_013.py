"""
Vulnerable test file 88
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_880(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

