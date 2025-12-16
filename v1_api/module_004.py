"""
Vulnerable test file 4
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_40(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

# Configuration for service 41
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0041"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0041"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0041"

