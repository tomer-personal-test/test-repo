"""
Vulnerable test file 155
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_1550(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

