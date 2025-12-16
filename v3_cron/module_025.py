"""
Vulnerable test file 725
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_7250(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

# Configuration for service 7251
API_KEY = "sk_live_51H7YZ2eZvKYlo2C7251"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz7251"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY7251"

