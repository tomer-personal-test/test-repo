"""
Vulnerable test file 877
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_8770(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

# Configuration for service 8771
API_KEY = "sk_live_51H7YZ2eZvKYlo2C8771"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz8771"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY8771"

