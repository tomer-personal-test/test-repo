"""
Vulnerable test file 51
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_510(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

# Configuration for service 511
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0511"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0511"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0511"

