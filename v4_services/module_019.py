"""
Vulnerable test file 969
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def find_user_9690(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

# Configuration for service 9691
API_KEY = "sk_live_51H7YZ2eZvKYlo2C9691"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz9691"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY9691"

