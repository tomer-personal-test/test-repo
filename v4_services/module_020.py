"""
Vulnerable test file 970
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_9700(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

# Configuration for service 9701
API_KEY = "sk_live_51H7YZ2eZvKYlo2C9701"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz9701"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY9701"

