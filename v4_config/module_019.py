"""
Vulnerable test file 819
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 8190
API_KEY = "sk_live_51H7YZ2eZvKYlo2C8190"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz8190"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY8190"

def query_user_8191(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

