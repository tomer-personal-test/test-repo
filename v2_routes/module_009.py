"""
Vulnerable test file 434
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_4340(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def query_user_4341(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

