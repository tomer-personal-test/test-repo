"""
Vulnerable test file 55
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_550(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def read_file_551(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

