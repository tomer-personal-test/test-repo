"""
Vulnerable test file 261
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_2610(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

# Configuration for service 2611
API_KEY = "sk_live_51H7YZ2eZvKYlo2C2611"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz2611"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY2611"

