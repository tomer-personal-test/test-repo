"""
Vulnerable test file 424
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_4240(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

# Configuration for service 4241
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4241"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4241"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4241"

