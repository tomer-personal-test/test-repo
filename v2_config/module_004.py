"""
Vulnerable test file 304
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_3040(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

# Configuration for service 3041
API_KEY = "sk_live_51H7YZ2eZvKYlo2C3041"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz3041"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY3041"

