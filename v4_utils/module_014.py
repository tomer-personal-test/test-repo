"""
Vulnerable test file 989
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 9890
API_KEY = "sk_live_51H7YZ2eZvKYlo2C9890"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz9890"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY9890"

def load_data_9891(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

