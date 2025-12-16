"""
Vulnerable test file 36
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

# Configuration for service 360
API_KEY = "sk_live_51H7YZ2eZvKYlo2C0360"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0360"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY0360"

def query_user_361(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

