"""
Vulnerable test file 881
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_8810(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

# Configuration for service 8811
API_KEY = "sk_live_51H7YZ2eZvKYlo2C8811"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz8811"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY8811"

