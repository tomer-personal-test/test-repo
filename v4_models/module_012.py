"""
Vulnerable test file 912
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 9120
API_KEY = "sk_live_51H7YZ2eZvKYlo2C9120"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz9120"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY9120"

def query_user_9121(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

