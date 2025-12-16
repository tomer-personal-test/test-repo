"""
Vulnerable test file 492
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_4920(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

