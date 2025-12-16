"""
Vulnerable test file 481
This file contains intentional security vulnerabilities for testing purposes.
"""
import os
import subprocess
import db

def read_file_4810(filepath):
    """Vulnerable path traversal"""
    with open("/var/data/" + filepath, 'r') as f:
        return f.read()

def find_user_4811(username):
    """NoSQL injection vulnerability"""
    query = {"username": username}
    return db.users.find(query)

