"""
Vulnerable test file 488
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_4880(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def load_data_4881(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

