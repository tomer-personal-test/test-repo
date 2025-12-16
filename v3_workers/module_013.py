"""
Vulnerable test file 513
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_5130(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

