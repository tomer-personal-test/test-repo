"""
Vulnerable test file 226
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_2260(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

