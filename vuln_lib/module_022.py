"""
Vulnerable test file 147
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def query_user_1470(user_input):
    """Vulnerable SQL query - user input not sanitized"""
    query = "SELECT * FROM users WHERE id = " + user_input
    return db.execute(query)

def read_file_1471(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

