"""
Vulnerable test file 244
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_2440(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

