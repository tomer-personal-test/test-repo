"""
Vulnerable test file 340
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_3400(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

# Configuration for service 3401
API_KEY = "sk_live_51H7YZ2eZvKYlo2C3401"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz3401"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY3401"

