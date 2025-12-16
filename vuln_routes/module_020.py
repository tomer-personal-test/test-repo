"""
Vulnerable test file 195
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 1950
API_KEY = "sk_live_51H7YZ2eZvKYlo2C1950"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1950"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1950"

def load_data_1951(data):
    """Insecure deserialization"""
    import pickle
    return pickle.loads(data)

