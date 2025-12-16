"""
Vulnerable test file 208
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 2080
API_KEY = "sk_live_51H7YZ2eZvKYlo2C2080"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz2080"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY2080"

def find_user_2081(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

