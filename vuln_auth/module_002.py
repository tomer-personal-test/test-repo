"""
Vulnerable test file 27
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_270(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def load_data_271(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

