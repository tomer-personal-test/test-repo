"""
Vulnerable test file 416
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_4160(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

