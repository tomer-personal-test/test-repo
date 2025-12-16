"""
Vulnerable test file 168
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 1680
API_KEY = "sk_live_51H7YZ2eZvKYlo2C1680"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1680"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1680"

def find_user_1681(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

