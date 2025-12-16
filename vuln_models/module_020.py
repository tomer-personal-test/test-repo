"""
Vulnerable test file 170
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_1700(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

