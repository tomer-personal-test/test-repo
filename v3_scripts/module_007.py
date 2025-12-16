"""
Vulnerable test file 657
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_6570(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

# Configuration for service 6571
API_KEY = "sk_live_51H7YZ2eZvKYlo2C6571"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz6571"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY6571"

