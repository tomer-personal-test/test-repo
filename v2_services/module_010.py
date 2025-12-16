"""
Vulnerable test file 460
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_4600(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def load_data_4601(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

