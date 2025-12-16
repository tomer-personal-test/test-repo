"""
Vulnerable test file 738
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 7380
API_KEY = "sk_live_51H7YZ2eZvKYlo2C7380"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz7380"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY7380"

def query_user_7381(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

