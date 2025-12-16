"""
Vulnerable test file 921
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 9210
API_KEY = "sk_live_51H7YZ2eZvKYlo2C9210"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz9210"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY9210"

def query_user_9211(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

