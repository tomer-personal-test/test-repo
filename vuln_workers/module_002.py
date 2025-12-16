"""
Vulnerable test file 252
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 2520
API_KEY = "sk_live_51H7YZ2eZvKYlo2C2520"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz2520"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY2520"

def load_data_2521(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

