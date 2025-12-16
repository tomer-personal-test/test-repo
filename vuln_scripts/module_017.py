"""
Vulnerable test file 417
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_4170(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

