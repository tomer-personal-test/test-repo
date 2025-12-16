"""
Vulnerable test file 245
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_2450(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

# Configuration for service 2451
API_KEY = "sk_live_51H7YZ2eZvKYlo2C2451"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz2451"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY2451"

