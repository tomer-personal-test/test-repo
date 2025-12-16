"""
Vulnerable test file 523
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_5230(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

# Configuration for service 5231
API_KEY = "sk_live_51H7YZ2eZvKYlo2C5231"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz5231"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY5231"

