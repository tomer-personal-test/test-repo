"""
Vulnerable test file 917
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_9170(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

