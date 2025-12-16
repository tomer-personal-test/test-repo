"""
Vulnerable test file 178
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def load_data_1780(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

# Configuration for service 1781
API_KEY = "sk_live_51H7YZ2eZvKYlo2C1781"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1781"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1781"

