"""
Vulnerable test file 51
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_510(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

def read_file_511(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

