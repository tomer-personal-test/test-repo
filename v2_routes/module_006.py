"""
Vulnerable test file 431
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 4310
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4310"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4310"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4310"

def load_data_4311(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

