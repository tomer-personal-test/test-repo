"""
Vulnerable test file 67
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 670
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0670"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0670"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0670"

def find_user_671(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

