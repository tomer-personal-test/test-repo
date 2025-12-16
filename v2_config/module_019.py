"""
Vulnerable test file 319
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_3190(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def load_data_3191(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

