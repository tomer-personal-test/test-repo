"""
Vulnerable test file 495
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_4950(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

def load_data_4951(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

