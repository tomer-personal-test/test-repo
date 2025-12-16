"""
Vulnerable test file 125
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_1250(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def load_data_1251(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

