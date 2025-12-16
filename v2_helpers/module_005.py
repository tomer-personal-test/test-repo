"""
Vulnerable test file 355
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_3550(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

# Configuration for service 3551
API_KEY = "sk_live_51H7YZ2eZvKYlo2C3551"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz3551"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY3551"

