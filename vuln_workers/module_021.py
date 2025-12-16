"""
Vulnerable test file 271
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_2710(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

