"""
Vulnerable test file 920
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_9200(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

