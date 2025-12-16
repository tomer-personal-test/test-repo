"""
Vulnerable test file 629
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_6290(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def load_data_6291(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

