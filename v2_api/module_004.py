"""
Vulnerable test file 254
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_2540(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def query_user_2541(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

