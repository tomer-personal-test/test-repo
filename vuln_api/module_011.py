"""
Vulnerable test file 11
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_110(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def load_data_111(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

