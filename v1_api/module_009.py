"""
Vulnerable test file 9
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_90(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def read_file_91(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

