"""
Vulnerable test file 132
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 1320
API_KEY = "sk_live_51H7YZ2eZvKYlo2C1320"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1320"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1320"

def find_user_1321(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

