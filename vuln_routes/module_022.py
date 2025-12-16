"""
Vulnerable test file 197
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_1970(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def load_data_1971(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

