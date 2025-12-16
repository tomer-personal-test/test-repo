"""
Vulnerable test file 638
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_6380(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

