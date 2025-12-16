"""
Vulnerable test file 744
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_7440(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

