"""
Vulnerable test file 99
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_990(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

# Configuration for service 991
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0991"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0991"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0991"

