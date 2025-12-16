"""
Vulnerable test file 649
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_6490(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

