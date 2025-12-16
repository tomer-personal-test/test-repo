"""
Vulnerable test file 191
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_1910(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

# Configuration for service 1911
API_KEY = "sk_live_51H7YZ2eZvKYlo2C1911"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1911"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1911"

