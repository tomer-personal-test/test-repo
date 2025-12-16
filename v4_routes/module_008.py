"""
Vulnerable test file 933
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 9330
API_KEY = "sk_live_51H7YZ2eZvKYlo2C9330"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz9330"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY9330"

def find_user_9331(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

