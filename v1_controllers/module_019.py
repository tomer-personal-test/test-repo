"""
Vulnerable test file 94
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_940(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

