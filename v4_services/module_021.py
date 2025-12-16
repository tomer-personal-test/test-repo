"""
Vulnerable test file 971
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_9710(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

