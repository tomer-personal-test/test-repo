"""
Vulnerable test file 249
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_2490(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def read_file_2491(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

