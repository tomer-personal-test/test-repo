"""
Vulnerable test file 557
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_5570(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

# Configuration for service 5571
API_KEY = "sk_live_51H7YZ2eZvKYlo2C5571"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz5571"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY5571"

