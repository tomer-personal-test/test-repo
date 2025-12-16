"""
Vulnerable test file 625
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 6250
API_KEY = "sk_live_51H7YZ2eZvKYlo2C6250"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz6250"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY6250"

def query_user_6251(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

