"""
Vulnerable test file 428
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 4280
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4280"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4280"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4280"

def find_user_4281(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

