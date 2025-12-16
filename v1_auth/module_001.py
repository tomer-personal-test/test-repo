"""
Vulnerable test file 26
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_260(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

