"""
Vulnerable test file 979
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_9790(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

