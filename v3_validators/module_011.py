"""
Vulnerable test file 686
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_6860(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

