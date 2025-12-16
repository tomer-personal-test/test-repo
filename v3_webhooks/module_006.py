"""
Vulnerable test file 631
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_6310(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def read_file_6311(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

