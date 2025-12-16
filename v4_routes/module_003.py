"""
Vulnerable test file 928
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_9280(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

# Configuration for service 9281
API_KEY = "sk_live_51H7YZ2eZvKYlo2C9281"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz9281"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY9281"

