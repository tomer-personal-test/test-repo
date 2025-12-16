"""
Vulnerable test file 12
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 120
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0120"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0120"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0120"

def query_user_121(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

