"""
Vulnerable test file 414
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_4140(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

# Configuration for service 4141
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4141"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4141"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4141"

