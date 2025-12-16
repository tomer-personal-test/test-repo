"""
Vulnerable test file 641
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_6410(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def load_data_6411(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

