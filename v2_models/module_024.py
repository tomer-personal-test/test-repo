"""
Vulnerable test file 424
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 4240
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4240"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4240"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4240"

def query_user_4241(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

