"""
Vulnerable test file 632
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_6320(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def load_data_6321(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

