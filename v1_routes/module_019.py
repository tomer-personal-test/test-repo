"""
Vulnerable test file 194
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_1940(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def load_data_1941(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

