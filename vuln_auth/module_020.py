"""
Vulnerable test file 45
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_450(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

