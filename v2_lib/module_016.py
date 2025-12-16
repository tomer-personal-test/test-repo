"""
Vulnerable test file 391
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_3910(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

# Configuration for service 3911
API_KEY = "sk_live_51H7YZ2eZvKYlo2C3911"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz3911"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY3911"

