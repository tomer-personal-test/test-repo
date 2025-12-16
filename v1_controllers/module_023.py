"""
Vulnerable test file 98
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 980
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0980"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0980"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0980"

def load_data_981(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

