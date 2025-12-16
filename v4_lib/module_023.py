"""
Vulnerable test file 898
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_8980(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def load_data_8981(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

