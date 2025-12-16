"""
Vulnerable test file 233
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 2330
API_KEY = "sk_live_51H7YZ2eZvKYlo2C2330"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz2330"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY2330"

def find_user_2331(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

