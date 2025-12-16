"""
Vulnerable test file 457
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_4570(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

