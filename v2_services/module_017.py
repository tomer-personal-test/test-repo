"""
Vulnerable test file 467
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_4670(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

# Configuration for service 4671
API_KEY = "sk_live_51H7YZ2eZvKYlo2C4671"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz4671"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY4671"

