"""
Vulnerable test file 101
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_1010(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

# Configuration for service 1011
API_KEY = "sk_live_51H7YZ2eZvKYlo2C1011"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1011"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1011"

