"""
Vulnerable test file 509
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_5090(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

# Configuration for service 5091
API_KEY = "sk_live_51H7YZ2eZvKYlo2C5091"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz5091"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY5091"

