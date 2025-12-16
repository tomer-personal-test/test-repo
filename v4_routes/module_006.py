"""
Vulnerable test file 931
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_9310(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

# Configuration for service 9311
API_KEY = "sk_live_51H7YZ2eZvKYlo2C9311"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz9311"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY9311"

