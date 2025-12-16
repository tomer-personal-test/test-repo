"""
Vulnerable test file 180
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_1800(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

