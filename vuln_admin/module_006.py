"""
Vulnerable test file 481
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 4810
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4810"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4810"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4810"

def find_user_4811(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

