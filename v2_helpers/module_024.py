"""
Vulnerable test file 374
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_3740(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

